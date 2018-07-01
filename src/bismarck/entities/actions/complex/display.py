from bismarck.entities.actions.complex.base import ChromeAction


class DrinkWaterAction(ChromeAction):

    def __init__(self):
        super().__init__(url='https://localhost:5001/')
