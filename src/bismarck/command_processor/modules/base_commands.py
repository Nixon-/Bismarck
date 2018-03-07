import subprocess

from bismarck.command_processor.command_processor import CommandModule


class ScreenController(CommandModule):

    WAKE_UP_COMMAND = 'gsettings set org.gnome.desktop.screensaver idle-activation-enabled false'
    SLEEP_COMMAND = 'gsettings set org.gnome.desktop.screensaver idle-activation-enabled true'

    def wakeup(self):
        proc = subprocess.Popen(self.WAKE_UP_COMMAND, shell=True)
        proc.wait()

    def sleep(self):
        proc = subprocess.Popen(self.SLEEP_COMMAND,  shell=True)
        proc.wait()


if __name__ == "__main__":
    import time
    screen = ScreenController()
    while True:
        screen.sleep()
        time.sleep(30)
        screen.wakeup()
        time.sleep(30)
