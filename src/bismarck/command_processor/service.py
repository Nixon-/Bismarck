from bismarck.service.service import HostedService


class CommandApi(HostedService):

    def __init__(self):
        super().__init__("Bismarck")

    def start(self):
        self.host.start()
