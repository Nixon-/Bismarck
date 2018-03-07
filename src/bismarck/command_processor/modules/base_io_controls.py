import pyautogui

from bismarck.command_processor.command_processor import CommandModule


class MouseControl(CommandModule):

    def __init__(self):
        self._position = list(pyautogui.position())
        self.bounds = list(pyautogui.size())

    def move_mouse_from_current(self, x, y):
        self._position = list(pyautogui.position())
        self.position[0] += x
        self.position[1] += y
        self._move()

    def move_mouse_to_absolute(self, x, y):
        self.position = (x, y)
        self._move()

    @property
    def position(self):
        return tuple(self._position)

    @position.setter
    def position(self, position):
        self._position = list(position)
        self._move()

    def _move(self):
        for i in range(len(self._position)):
            self._position[i] = sorted((0, self._position[i], self.bounds[i]))[1]
        pyautogui.moveTo(self._position)
        print(pyautogui.position())
