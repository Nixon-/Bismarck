from bismarck.entities.actions.complex.display import DrinkWaterAction
from bismarck.entities.actions.complex.financial import QuestradeAction, LendingLoopAction
from bismarck.entities.actions.complex.google_actions import GoogleCalendarAction

complex_actions = {
    'calendar': lambda: GoogleCalendarAction(),
    'questrade': lambda: QuestradeAction(),
    'lending loop': lambda: LendingLoopAction(),
    'drink water': lambda: DrinkWaterAction()
}


def get_complex_action(intent):
    action = complex_actions.get(intent, None)
    if action is not None:
        action = action()
    return action
