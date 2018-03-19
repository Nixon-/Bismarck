

class Action(dict):

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


class ComplexAction:

    def __init__(self):
        self.actions = list()

    def next_action(self):
        for action in self.actions:
            yield action

    def add_action(self, action):
        self.actions.append(action)
