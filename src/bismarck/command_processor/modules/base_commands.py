from bismarck.command_processor.modules.base_io_controls import MouseControl


def wakeup_screen():
    mouse = MouseControl()
    bounds = list(mouse.bounds)
    center = [bounds[0]/2.0, bounds[1]/2.0]
    current_position = list(mouse.position)
    if center == current_position:
        jitter_mouse = (1, 1)
    else:
        x = 1 if current_position[0] < center[0] else -1
        y = 1 if current_position[1] < center[1] else -1
        jitter_mouse = (x, y)
    mouse.move_mouse_from_current(*jitter_mouse)


if __name__ == "__main__":
    import time
    while True:
        wakeup_screen()
        time.sleep(65)
