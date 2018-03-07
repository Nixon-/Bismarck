import subprocess


def wakeup_screen():
    proc = subprocess.Popen('gsettings set org.gnome.desktop.screensaver idle-activation-enabled false', shell=True)
    proc.wait()


def sleep_screen():
    proc = subprocess.Popen('gsettings set org.gnome.desktop.screensaver idle-activation-enabled true', shell=True)
    proc.wait()


if __name__ == "__main__":
    import time
    while True:
        wakeup_screen()
        time.sleep(10)
        sleep_screen()
        time.sleep(10)
