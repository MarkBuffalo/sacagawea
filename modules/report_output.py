import glob
from collections import defaultdict
from pathlib import Path
from datetime import datetime


class ReportOutput:
    def __init__(self, **kwargs):
        self.img_dict = defaultdict(list)
        self.report_type = kwargs.get("scan_mode")
        self.figure_caption = '<figure class="figure"><figcaption class="figure-caption" class="p%">$:%</figcaption><img src="replacemenow" class="figure-img img-fluid rounded" alt="A screeshot of the host $ and accompanying port, %"></figure>'

    @staticmethod
    def get_host_info(image_name):
        return Path(image_name).stem

    def load_report_info(self):
        images = glob.glob("shots/*")

        figure_html = ""

        for img in images:
            file_name = self.get_host_info(img)

            host = file_name
            port = 0

            if self.report_type == "single":
                host = file_name
                port = ""
            if "_" in file_name:
                host = file_name.split("_")[0]
                port = file_name.split("_")[1]

            self.img_dict[host].append(port)
            # Need to fix this to include hosts and ports.

            if port == 0:
                figure_html += self.figure_caption.replace(
                    "replacemenow",
                    f"../{img}").replace("$", host).replace("%", "") + "\n"
            else:
                figure_html += self.figure_caption.replace(
                    "replacemenow",
                    f"../{img}").replace("$", host).replace("%", str(port)) + "\n"

        start_html = ""
        with open("reports/templates/start.html", "r") as start:
            start_html = start.read()

        end_html = ""
        with open("reports/templates/end.html", "r") as end:
            end_html = end.read()

        self.write_report(start_html, end_html, figure_html)

    @staticmethod
    def write_report(start_html, end_html, figure_html):
        current_time = datetime.today().strftime('%Y-%m-%d %H_%M_%S')
        with open(f"reports/report-{current_time}.html", "w") as w:
            final_html = ""

            final_html += start_html
            final_html = final_html.replace("%^%", figure_html)
            final_html += end_html

            w.write(final_html)

