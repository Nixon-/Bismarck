from bismarck.entities.action import ActionChain
from bismarck.entities.actions.actions import OpenBrowserAction, GoToUrlAction


class ChromeAction(ActionChain):

    def __init__(self, url=None):
        super().__init__()
        self.url = url
        # Open or focus the browser
        self.add_action(OpenBrowserAction())
        # Go to url
        self.add_action(GoToUrlAction(self.url))