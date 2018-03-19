from bismarck.command_processor.modules.io.base_commands import Display
from bismarck.command_processor.modules.io.base_io_controls import MouseController
from bismarck.service.service import HostedService


class IoService(HostedService):

    service_name = "io_service"

    def __init__(self):
        super().__init__(self.service_name)
        self.controller = MouseController()
        self.display = Display()

    def start(self):
        super().start()
