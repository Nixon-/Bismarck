from abc import ABC, abstractmethod


class Action(dict, ABC):

    _name_field = 'name'
    _service_endpoint = 'url'
    _params_field = 'params'

    def __init__(self, name, url, params):
        super().__init__()
        self[self._name_field] = name
        self[self._service_endpoint] = url
        self[self._params_field] = params

    @property
    def name(self):
        return self[self._name_field]
    
    @property
    def params(self):
        return self[self._params_field]

    @property
    def api_endpoint(self):
        return self[self._service_endpoint]

    def save(self):
        return dict(self)

    @abstractmethod
    def execute(self):
        raise NotImplemented()


class ActionChain:

    def __init__(self):
        self._actions = list()

    def add_action(self, action):
        self._actions.append(action)

    def execute(self):
        for action in self._actions:
            action.execute()

    def save(self):
        return [action.save() for action in self._actions]

    def load(self, dumped_actions):
        self._actions = list(map(lambda x: Action(**x), dumped_actions))
