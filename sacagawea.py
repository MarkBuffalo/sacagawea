#!/usr/bin/env python3

# coding=utf-8
import argparse
import sys
import os
from portscan import PortScan
from queue import Queue
from thread_handler import ThreadWorker
from banner import Banner
from print_methods import ct_print, colorize_bar_output
from web_driver import WebDriver
from report_output import ReportOutput
from tqdm import tqdm
from colorama import Fore


class Sacagawea:
    def __init__(self):
        # Disable Selenium startup messages.
        os.environ['WDM_LOG_LEVEL'] = '0'
        self.banner = Banner()

        self.port_scanner = PortScan()
        self.queue = Queue(maxsize=0)
        self.queue_threads = 75
        self.report = ReportOutput()

        # Command Line Arguments
        self.parser = argparse.ArgumentParser(description='Sacagawea The Explorer')
        self.parser.add_argument('-i', '--inputfile', help="Specify a text file with line-separated domains")
        self.parser.add_argument('-b', '--browser',
                                 help="The browser driver to use. e.g.: firefox/chrome. Default is Firefox.")
        self.parser.add_argument('-c', '--cidr',
                                 help="CIDR Range to use in lieu of --inputfile.")
        self.parser.add_argument('-r', '--report',
                                 action="store_true",
                                 help="Regenerate the report instead of running another long-winded scan.")
        self.args = self.parser.parse_args()

        self.current_browser = "firefox"
        self.driver = WebDriver()
        self.input_file = ""
        self.target_list = []

        self.progress_bar = None
        self.r_bar = colorize_bar_output("| Host: {n_fmt} of {total_fmt} | Elapsed: {elapsed} | Remaining: "
                                         "{remaining} | Rate: {rate_fmt}{postfix} ")
        self.bar = f"{Fore.LIGHTGREEN_EX}{{bar}}"
        self.l_bar = colorize_bar_output("[{desc}: {percentage:3.0f}%] ")

    def run_actions_threaded(self, **kwargs):
        for i in range(self.queue_threads):
            """This takes the queue item, then the SiteChecker class, and the "examine_domain" function within the
            SiteChecker class, followed by the examine_domain() function with the progress bar and arguments."""
            worker = ThreadWorker(**kwargs)
            worker.daemon = True
            worker.start()
        self.queue.join()

    @staticmethod
    def check_output_directory():
        if not os.path.exists("shots/"):
            os.makedirs("shots/")

    def load_target_list(self):
        queue = Queue(maxsize=0)
        try:
            with open(self.input_file, "r") as f:
                self.target_list.extend(f.read().splitlines())

                for target in self.target_list:
                    queue.put(target.rstrip())
        except FileNotFoundError:
            print(f"[?] File not found: {self.input_file}")
        except Exception as e:
            print(f"[?] There was a problem opening [{self.input_file}]: Error message:[{str(e)}]")
        return queue

    def explore(self):
        if not self.args.cidr and not self.args.inputfile:
            self.parser.print_help()
            sys.exit(0)

        # If CIDR is selected, grab the CIDR list and then run the scan.
        if self.args.cidr:
            self.target_list.extend(self.port_scanner.get_ip_range_from_cidr(self.args.cidr))
            for target in self.target_list:
                self.queue.put(target)
            ct_print(f"[!] Loaded target list from {self.args.cidr}")
            ct_print(f"[!] {self.args.cidr} was parsed into {self.queue.qsize()} host(s).")

        if self.args.inputfile:
            self.queue = self.load_target_list()
            ct_print(f"[!] Loaded target list from {self.args.inputfile}")
            ct_print(f"[!] {self.args.cidr} was parsed into {self.queue.qsize()} host(s).")

        # Which web driver are we using? Firefox' GeckoDriver is default.
        if self.args.browser == "chrome":
            self.current_browser = "chrome"

        # Check hosts. We want to give the user the flexibility to choose both the CIDR range and from a list of hosts,
        # so we'll use self.check_hosts() after we've gone through the motions of loading the self.target_list.
        self.check_hosts()

    def check_hosts(self):
        self.progress_bar = tqdm(total=self.queue.qsize(), file=sys.stdout, unit=' sites',
                                 bar_format=f"{self.l_bar}{self.bar}{self.r_bar}", dynamic_ncols=True,
                                 desc="Sacagawea Progress", leave=False)

        self.run_actions_threaded(queue=self.queue, class_name=self.port_scanner,
                                  driver=self.driver, function_name="check_site", progress_bar=self.progress_bar)
        self.progress_bar.close()


if __name__ == "__main__":
    sacagawea = Sacagawea()
    try:
        sacagawea.explore()
    except KeyboardInterrupt:
        sys.exit(0)
