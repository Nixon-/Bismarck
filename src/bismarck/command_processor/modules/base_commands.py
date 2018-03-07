import subprocess

from bismarck.command_processor.command_processor import CommandModule
from bismarck.command_processor.modules.base_io_controls import MouseController


class ScreenController(CommandModule):

    SLEEP_COMMAND = 'gsettings set org.gnome.desktop.screensaver idle-activation-enabled false'
    WAKE_UP_COMMAND = 'gsettings set org.gnome.desktop.screensaver idle-activation-enabled true'

    def wakeup(self):
        mouse = MouseController()
        mouse.move_mouse_to_absolute(0,0)


if __name__ == "__main__":
    import time
    screen = ScreenController()
    while True:
        screen.sleep()
        time.sleep(30)
        screen.wakeup()
        time.sleep(30)
