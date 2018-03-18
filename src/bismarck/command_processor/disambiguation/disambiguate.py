from http import HTTPStatus

from bismarck.service.service import HostedService, get_response_for


class SemanticAnalyzer(HostedService):

    service_name = "semantic_analysis"

    def __init__(self):
        super().__init__(self.service_name)

    def start(self):
        self.host.add_endpoint('get_module_for_action', 'get_module_for_action', self.get_intention)
        self.host.start()

    def get_intention(self, url_args, *args, **kwargs):
        return get_response_for(HTTPStatus.OK)
