from bismarck.command_processor.command_processor import CommandModule
from selenium import webdriver


class ChromeController(CommandModule):

    _browser_path = ""

    def __init__(self):
        super().__init__()
        self.driver = None

    def open_browser(self):
        self.driver = webdriver.Chrome(executable_path=)

    def go_to_address(self):
        pass


if __name__ == "__main__":
    controller = ChromeController()
    controller.open_browser()
