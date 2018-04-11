from bismarck.entities.actions.actions import EnterDataAction, FormSubmitAction
from bismarck.entities.actions.complex.base import ChromeAction


class QuestradeAction(ChromeAction):

    def __init__(self):
        super().__init__(url='https://my.questrade.com/trading/account/balances')
        self.add_action(EnterDataAction(where='ctl00_DefaultContent_txtUsername', text='questrade/username'))
        self.add_action(EnterDataAction(where='ctl00_DefaultContent_txtPassword', text='questrade/password'))
        self.add_action(FormSubmitAction(where='ctl00_DefaultContent_btnLogin'))


class LendingLoopAction(ChromeAction):

    def __init__(self):
        super().__init__(url='https://www.lendingloop.ca/dashboard')
        self.add_action(EnterDataAction(where='user_email', text='lendingloop/username'))
        self.add_action(EnterDataAction(where='user_password', text='lendingloop/password'))
        self.add_action(FormSubmitAction(where='user_email'))
