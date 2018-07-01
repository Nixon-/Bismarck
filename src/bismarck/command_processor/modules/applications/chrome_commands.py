from selenium.webdriver.common.by import By

from bismarck.command_processor.command_processor import CommandModule
from selenium import webdriver


class ChromeController(CommandModule):

    _browser_path = "../utils/chromedriver"

    def __init__(self, secret_handler):
        super().__init__()
        self.secret_handler = secret_handler
        self.driver = None
        self.current_page = None

    def open_browser(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(chrome_options=options) #, executable_path=self._browser_path)

    def go_to_address(self, url):
        self.current_page = self.driver.get(url)

    def enter_text(self, where, text):
        if '/' in where:
            element, ident = where.split('/')
        else:
            element, ident = 'id', where
        if '/' in text:
            set_name, param = text.split('/')
            data = self.secret_handler.get_information_set(set_name)
            tag = data[param]
        else:
            tag = text
        getattr(self.driver, 'find_element_by_{}'.format(element))(ident).send_keys(tag)

    def submit(self, where):
        if '/' in where:
            element, ident = where.split('/')
        else:
            element, ident = 'id', where
        getattr(self.driver, 'find_element_by_{}'.format(element))(ident).submit()


if __name__ == "__main__":
    controller = ChromeController()
