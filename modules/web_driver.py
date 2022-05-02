from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService

from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService

from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
import time


class WebDriver:
    def __init__(self):
        self.chrome_options = ChromeOptions()
        self.chrome_options.ignore_certificate_errors = True
        self.chrome_options.headless = True

        self.firefox_options = FirefoxOptions()
        self.firefox_options.headless = True
        self.firefox_options.accept_insecure_certs = True

        self.firefox_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),
                                                options=self.firefox_options)

        self.chrome_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                                               options=self.chrome_options)
        self.current_browser = "firefox"

    @staticmethod
    def get_domain_from_url(url):
        # Format is https://www.google.com:8443/sdf/sdlf;sdlf;sdlf/sdf//dsf/sd/fsd/fsd/lf?sdzf-=pwe3riojksdf=KLSQKLAFLK
        # Returns: www.google.com:8443 - we can parse the port later.
        # If no port is specified, then it won't be included.
        # Must include the www, and not just the host name,
        # or we could potentially run into parsing problems later down the road.
        return url.split("/")[2]

    def take_screenshot(self, url):
        if self.current_browser == "firefox":
            self.firefox_driver.get(url)
            self.firefox_driver.save_screenshot(f"shots/{self.get_domain_from_url(url).replace(':', '_')}.png")
        else:
            self.chrome_driver.get(url)
            self.chrome_driver.save_screenshot(f"shots/{self.get_domain_from_url(url).replace(':', '_')}.png")

