from bismarck.entities.Action import ComplexAction

complex_actions = {
    'calendar': lambda: GoogleCalendarAction()
}


class GoogleCalendarAction(ComplexAction):

    def __init__(self):
        super().__init__()
        # Open or focus the browser
        self.add_action()
        # Go to google calendar
        self.add_action()
        # Check if we're showing the calendar
        self.add_action()
        # Check for end state
        self.add_action()


def get_complex_actions(intent):
    return complex_actions[intent]()
