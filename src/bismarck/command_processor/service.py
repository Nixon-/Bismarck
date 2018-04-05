import urllib.error
from queue import Empty

from multiprocessing import Process, Queue

from bismarck.disambiguation.disambiguate import SemanticAnalyzer
from bismarck.entities.action import ActionChain
from bismarck.entities.actions.actions import get_action
from bismarck.entities.complex_action import get_complex_action
from bismarck.service.requests import api_get
from bismarck.service.service import HostedService, get_response_for
from http import HTTPStatus


class CommandApi(HostedService):

    service_name = "Bismarck"

    def __init__(self):
        super().__init__(self.service_name)

    def start(self):
        self.add_api_action('do_action', self.do_action)
        self.host.start()

    def add_api_action(self, name, action_fx, methods=('GET', 'POST')):
        self.host.add_endpoint('api/{}'.format(name), name, action_fx, methods=methods)

    @staticmethod
    def do_action(url_args, *args, **kwargs):
        try:
            for key in url_args.keys():
                url_args[key] = url_args[key][0]
            api_get(Coordinator.service_name, 'new_command', url_args)
            return get_response_for(HTTPStatus.OK)
        except urllib.error.URLError:
            return get_response_for(HTTPStatus.INTERNAL_SERVER_ERROR)


class Coordinator(HostedService):

    service_name = "Coordinator"

    def __init__(self, num_workers=1):
        super().__init__(self.service_name)
        self.disambiguator = SemanticAnalyzer()
        self.action_queue = Queue()
        self.num_workers = num_workers
        self.workers = list()

    def start(self):
        self.host.add_endpoint('new_command', 'new_command', self.add_command_to_queue)
        self._start_workers()
        self.host.start()
        self._stop_workers()

    def _start_workers(self):
        def start_worker(action_queue, termination_code):
            Worker(action_queue=action_queue, termination_code=termination_code).start()

        for i in range(self.num_workers):
            self.workers.append(Process(target=start_worker, args=(self.action_queue, None)))
        for proc in self.workers:
            proc.start()

    def _stop_workers(self):
        self.action_queue.put({'name': Worker.termination_code})
        for proc in self.workers:
            proc.join()

    def add_command_to_queue(self, url_args, *args, **kwargs):
        self.action_queue.put(url_args)
        return get_response_for(HTTPStatus.OK)


class Worker:

    termination_code = '__terminate'

    def __init__(self, action_queue, termination_code=None):
        if termination_code is not None:
            self.termination_code = termination_code
        self.die = False
        self.command_queue = action_queue

    def start(self):
        while not self.die:
            try:
                action_dict = self.command_queue.get(block=True, timeout=5)
                for key in action_dict.keys():
                    action_dict[key] = action_dict[key][0]
                if action_dict['action_name'] == self.termination_code:
                    self.die = True
                    break
                action_chain = self.get_complex_action(action_dict)
                action_chain.execute()
            except Empty:
                pass
            except urllib.error.URLError:
                pass

    def get_complex_action(self, action_dict):
        action = get_complex_action(action_dict['application'].lower())
        if action is None:
            action = get_action(action_dict['application'])
        return action
