import glob
from collections import defaultdict
from pathlib import Path

class ReportOutput:
    def __init__(self):
        self.img_dict = defaultdict(list)

    @staticmethod
    def get_host_info(image_name):
        return Path(image_name).stem

    def load_report_info(self):
        images = glob.glob("../shots/*.png")

        new_html = ""

        for img in images:
            file_name = self.get_host_info(img)
            host = file_name.split("_")[0]
            port = file_name.split("_")[1]

            self.img_dict[host].append(port)

