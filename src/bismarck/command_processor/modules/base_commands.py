from bismarck.command_processor.modules.base_io_controls import MouseControl


def wakeup_screen():
    mouse_controller = MouseControl()
    jitter_mouse = (1, 1)
    mouse_controller.move_mouse_from_current(*jitter_mouse)


if __name__ == "__main__":
    wakeup_screen()