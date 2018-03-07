import pyautogui

from bismarck.command_processor.command_processor import CommandModule


class MouseControl(CommandModule):

    def __init__(self):
        self.position = list(pyautogui.position())
        self.bounds = pyautogui.size()

    def move_mouse_from_current(self, x, y):
        self.position[0] += x
        self.position[1] += y
        self._move()

    def move_mouse_to_absolute(self, x, y):
        self.position[0] = (x, y)
        self._move()

    def _move(self):
        for i in range(len(self.position)):
            self.position[i] = sorted((0, self.position[i], self.bounds[i]))[1]
        pyautogui.moveTo(self.position)
