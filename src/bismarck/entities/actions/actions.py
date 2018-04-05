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


class MoveMouseAction(Action):

    def __init__(self):
        super().__init__(name='', url='', params='')

    def execute(self):
        pass


def get_action(intent):
    raise NotImplementedError()
