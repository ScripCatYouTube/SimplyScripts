import keyboard
import time
import pyautogui

isClicking = False
isRUN = True

print(isClicking)

def set_clicker():
    global isClicking
    if isClicking:
        isClicking = False
        print('Off')
    else:
        isClicking = True
        print('On')

def _exit():
    global isRUN
    isRUN = False

keyboard.add_hotkey('Ctrl + z', set_clicker)
keyboard.add_hotkey('Alt + e', _exit)

while isRUN:
    if isClicking:
        pyautogui.click(button='left')
        #time.sleep(0.1)
print("Exit")