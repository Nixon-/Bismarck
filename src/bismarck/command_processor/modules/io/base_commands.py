from bismarck.command_processor.modules.io.base_io_controls import MouseController


class Display:

    def __init__(self):
        self.mouse = MouseController()

    def wakeup(self):
        bounds = list(self.mouse.bounds)
        pos = self.mouse.position
        new_pos = [
            0 if pos[0] > bounds[0] / 2.0 < 0 else bounds[0],
            0 if pos[1] > bounds[1] / 2.0 < 0 else bounds[1]
        ]
        self.mouse.move_mouse_to_absolute(*new_pos)


if __name__ == "__main__":
    import time
    screen = Display()
    while True:
        screen.wakeup()
        time.sleep(30)
