from bismarck.command_processor.command_processor import CommandModule
from bismarck.command_processor.modules.base_io_controls import MouseController


class ScreenController(CommandModule):

    SLEEP_COMMAND = 'gsettings set org.gnome.desktop.screensaver idle-activation-enabled false'
    WAKE_UP_COMMAND = 'gsettings set org.gnome.desktop.screensaver idle-activation-enabled true'

    def wakeup(self):
        mouse = MouseController()
        bounds = list(mouse.bounds)
        pos = mouse.position
        new_pos = [
            0 if pos[0] > bounds[0] / 2.0 < 0 else bounds[0],
            0 if pos[1] > bounds[1] / 2.0 < 0 else bounds[1]
        ]
        mouse.move_mouse_to_absolute(*new_pos)


if __name__ == "__main__":
    import time
    screen = ScreenController()
    while True:
        screen.wakeup()
        time.sleep(30)
