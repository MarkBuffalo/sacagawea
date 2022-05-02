import socket
import ipaddress
import sys
from contextlib import closing
from selenium.common.exceptions import TimeoutException, InvalidSessionIdException, WebDriverException
from modules.print_methods import ct_print

class PortScan:
    def __init__(self):
        self.common_web_port_list = [
            80,
            443,
            8080,
            8443
        ]

    @staticmethod
    def get_ip_range_from_cidr(cidr):
        return [str(ip) for ip in ipaddress.IPv4Network(cidr)]

    def check_site(self, **kwargs):
        ip = kwargs.get("param_input")
        driver = kwargs.get("driver")
        progress_bar = kwargs.get("progress_bar")

        try:
            open_ports = self.get_open_ports(ip)
            if open_ports:
                # This needs to be changed soon.
                # It needs to test if a TLS connection is available before assuming based on port numbers.
                for port in open_ports:
                    prefix = ""
                    if port == 80:
                        prefix = "http://"
                    elif port == 443:
                        prefix = "https://"
                    elif "443" in str(port):
                        prefix = "https://"
                    else:
                        prefix = "http://"
                    driver.take_screenshot(f"{prefix}{ip}:{port}")
            #ct_print(f"[!] Finished checking {ip}...")
            progress_bar.update(1)
        except socket.herror:
            return False
        except socket.gaierror:
            return False
        except socket.timeout:
            return False
        except socket.error:
            return False
        except TimeoutException:
            return False
        except InvalidSessionIdException:
            ct_print(f"[?] Strange error when attempting to scan {ip}. You may need to try again.")
            return False
        except WebDriverException:
            ct_print(f"[?] Web Driver blew up while attempting to connect to {ip}. You should manually check this host.")

    def get_open_ports(self, ip):
        open_ports = []
        for port in self.common_web_port_list:
            with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
                sock.settimeout(3)
                if sock.connect_ex((ip, port)) == 0:
                    sock.settimeout(None)
                    open_ports.append(port)
        if len(open_ports) > 0:
            return open_ports
        return None

    @staticmethod
    def is_port_open(ip, port):
        with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
            sock.settimeout(3)
            if sock.connect_ex((ip, port)) == 0:
                sock.settimeout(None)
                return True
            return False
