from bismarck.entities.action import ActionChain
from bismarck.entities.actions.actions import OpenBrowserAction, GoToUrlAction, EnterDataAction, FormSubmitAction

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
        self.add_action(EnterDataAction(where='user_email', text='google/email'))
        self.add_action(EnterDataAction(where='user_password', text='google/password'))
        self.add_action(FormSubmitAction(where=''))


class QuestradeAction(ChromeAction):

    def __init__(self):
        super().__init__(url='https://my.questrade.com/trading/account/balances')
        self.add_action(EnterDataAction(where='user_email', text='questrade/email'))
        self.add_action(EnterDataAction(where='user_password', text='questrade/password'))
        self.add_action(FormSubmitAction(where=''))


class LendingLoopAction(ChromeAction):

    def __init__(self):
        super().__init__(url='https://www.lendingloop.ca/dashboard')
        self.add_action(EnterDataAction(where='user_email', text='lending_loop/email'))
        self.add_action(EnterDataAction(where='user_password', text='lending_loop/password'))
        self.add_action(FormSubmitAction(where=''))


def get_complex_action(intent):
    action = complex_actions.get(intent, None)
    if action is not None:
        action = action()
    return action
