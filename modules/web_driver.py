from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService

from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService

from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager


class WebDriver:
    def __init__(self, **kwargs):
        self.chrome_options = ChromeOptions()
        self.chrome_options.ignore_certificate_errors = True
        self.chrome_options.headless = True

        self.firefox_options = FirefoxOptions()
        self.firefox_options.headless = True
        self.firefox_options.accept_insecure_certs = True

        self.browser = kwargs.get("browser")

    @staticmethod
    def get_domain_from_url(url):
        # Format is https://www.google.com:8443/sdf/sdlf;sdlf;sdlf/sdf//dsf/sd/fsd/fsd/lf?sdzf-=pwe3riojksdf=KLSQKLAFLK
        # Returns: www.google.com:8443 - we can parse the port later.
        # If no port is specified, then it won't be included.
        # Must include the www, and not just the host name,
        # or we could potentially run into parsing problems later down the road.
        return url.split("/")[2]

    def take_screenshot(self, url):
        if self.browser == "firefox":
            self.fire_browser_event(url, webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),
                                                           options=self.firefox_options))
        else:
            self.fire_browser_event(url, webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                                                          options=self.chrome_options))

    def fire_browser_event(self, url, driver):
        driver.set_window_size(1920, 1080)
        driver.get(url)
        driver.refresh()
        driver.save_screenshot(f"shots/{self.get_domain_from_url(url).replace(':', '_')}.png")
