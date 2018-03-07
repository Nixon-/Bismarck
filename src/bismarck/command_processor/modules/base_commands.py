from bismarck.command_processor.modules.base_io_controls import MouseControl
import time

def wakeup_screen():
    mouse_controller = MouseControl()
    jitter_mouse = (1, 1)
    while True:
        new_pos = list(mouse_controller.bounds)
        mouse_controller.move_mouse_to_absolute(new_pos[0]/2, new_pos[1]/2)
        time.sleep(5)
    #mouse_controller.move_mouse_from_current(*jitter_mouse)


if __name__ == "__main__":
    wakeup_screen()