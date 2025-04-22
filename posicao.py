import pyautogui
from time import sleep
def get_mouse_position():
    """
    Returns the current mouse position in the format (x=value, y=value)
    """
    x, y = pyautogui.position()
    return f"(x={x}, y={y})"

if __name__ == "__main__":
    sleep(5)
    print(get_mouse_position())
