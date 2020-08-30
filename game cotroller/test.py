from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

time.sleep(2)

for char in "This is my sentence":
    keyboard.press(char)
    keyboard.release(char)
    time.sleep(0.2)
