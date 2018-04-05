from bismarck.command_processor.command_processor import CommandModule
from selenium import webdriver


class ChromeController(CommandModule):

    _browser_path = "../utils/chromedriver"

    def __init__(self):
        super().__init__()
        self.driver = None
        self.current_page = None

    def open_browser(self):
        self.driver = webdriver.Chrome(executable_path=self._browser_path)

    def go_to_address(self, url):
        self.current_page = self.driver.get(url)


if __name__ == "__main__":
    controller = ChromeController()
