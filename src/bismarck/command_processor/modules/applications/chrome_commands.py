from selenium.webdriver.common.by import By

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

    def enter_text(self, where, text):
        if '/' in where:
            element, ident = where.split('/')
        else:
            element, ident = 'id', where
        if '/' in text:
            location, param = text.split('/')
            raise NotImplementedError()
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
