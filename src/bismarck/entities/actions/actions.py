from bismarck.command_processor.modules.applications.chrome_service import ChromeService
from bismarck.entities.action import Action
from bismarck.service.requests import api_get


class OpenBrowserAction(Action):

    def __init__(self):
        super().__init__(name='', url='', params='')

    def execute(self):
        api_get(ChromeService.service_name,  ChromeService.open_browser_request)


class GoToUrlAction(Action):

    def __init__(self, url):
        super().__init__(name='', url='', params='')
        self.url = url

    def execute(self):
        api_get(ChromeService.service_name, ChromeService.go_to_url_request, args={'url': self.url})


class EnterDataAction(Action):

    def __init__(self, where, text):
        super().__init__(name='', url='', params='')
        self.where = where
        self.text = text

    def execute(self):
        api_get(ChromeService.service_name, ChromeService.enter_text_request,
                args={'where': self.where, 'text': self.text})


class FormSubmitAction(Action):

    def __init__(self, where):
        super().__init__(name='', url='', params='')
        self.where = where

    def execute(self):
        api_get(ChromeService.service_name, ChromeService.submit_request, args={'where': self.where})


class MoveMouseAction(Action):

    def __init__(self):
        super().__init__(name='', url='', params='')

    def execute(self):
        pass


def get_action(intent):
    raise NotImplementedError()
