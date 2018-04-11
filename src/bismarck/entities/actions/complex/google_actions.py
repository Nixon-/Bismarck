from bismarck.entities.actions.actions import EnterDataAction, FormSubmitAction
from bismarck.entities.actions.complex.base import ChromeAction


class GoogleCalendarAction(ChromeAction):

    def __init__(self):
        super().__init__(url='https://calendar.google.com')
        # needs more complex navigation
        self.add_action(EnterDataAction(where='user_email', text='google/username'))
        self.add_action(EnterDataAction(where='user_password', text='google/password'))
        self.add_action(FormSubmitAction(where='user_password'))

