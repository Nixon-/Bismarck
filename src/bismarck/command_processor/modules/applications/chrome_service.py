from http import HTTPStatus

from bismarck.command_processor.modules.applications.chrome_commands import ChromeController
from bismarck.service.service import HostedService, get_response_for


class ChromeService(HostedService):

    service_name = "chrome_service"
    open_browser_request = 'open_browser'
    go_to_url_request = 'go_to_url'

    def __init__(self):
        super().__init__(self.service_name)
        self.controller = ChromeController()

    def start(self):
        self.host.add_endpoint(self.open_browser_request, self.open_browser_request, self.open_browser)
        self.host.add_endpoint(self.go_to_url_request, self.go_to_url_request, self.go_to_url)
        self.host.start()

    def open_browser(self, url_args, *args, **kwargs):
        try:
            self.controller.open_browser()
        except ValueError:
            pass
        return get_response_for(HTTPStatus.OK)

    def go_to_url(self, url_args, *args, **kwargs):
        url = url_args['url'][0]
        self.controller.go_to_address(url)
        return get_response_for(HTTPStatus.OK)
