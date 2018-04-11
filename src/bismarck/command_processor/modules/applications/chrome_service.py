from http import HTTPStatus

from bismarck.command_processor.modules.applications.chrome_commands import ChromeController
from bismarck.service.service import HostedService, get_response_for


class ChromeService(HostedService):

    service_name = "chrome_service"
    open_browser_request = 'open_browser'
    go_to_url_request = 'go_to_url'
    enter_text_request = 'enter_text'
    submit_request = 'submit'

    def __init__(self, secret_handler):
        super().__init__(self.service_name)
        self.controller = ChromeController(secret_handler)

    def start(self):
        self.host.add_endpoint(self.open_browser_request, self.open_browser_request, self.open_browser)
        self.host.add_endpoint(self.go_to_url_request, self.go_to_url_request, self.go_to_url)
        self.host.add_endpoint(self.enter_text_request, self.enter_text_request, self.enter_text)
        self.host.add_endpoint(self.submit_request, self.submit_request, self.submit)
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

    def enter_text(self, url_args, *args, **kwargs):
        text = url_args['text'][0]
        where = url_args['where'][0]
        self.controller.enter_text(where=where, text=text)
        return get_response_for(HTTPStatus.OK)

    def submit(self, url_args, *args, **kwargs):
        where = url_args['where'][0]
        self.controller.submit(where=where)
        return get_response_for(HTTPStatus.OK)
