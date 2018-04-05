from bismarck.entities.action import ActionChain
from bismarck.entities.actions.actions import OpenBrowserAction, GoToUrlAction

complex_actions = {
    'calendar': lambda: GoogleCalendarAction(),
    'questrade': lambda: QuestradeAction(),
    'lending loop': lambda: LendingLoopAction()
}


class ChromeAction(ActionChain):

    def __init__(self, url=None):
        super().__init__()
        self.url = url
        # Open or focus the browser
        self.add_action(OpenBrowserAction())
        # Go to url
        self.add_action(GoToUrlAction(self.url))


class GoogleCalendarAction(ChromeAction):

    def __init__(self):
        super().__init__(url='https://calendar.google.com')


class QuestradeAction(ChromeAction):

    def __init__(self):
        super().__init__(url='https://my.questrade.com/trading/account/balances')


class LendingLoopAction(ChromeAction):

    def __init__(self):
        super().__init__(url='https://www.lendingloop.ca/dashboard')


def get_complex_action(intent):
    action = complex_actions.get(intent, None)
    if action is not None:
        action = action()
    return action
