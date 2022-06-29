import pyperclip
import time
import pyautogui
import PIL.ImageGrab
import os

def get_color(location):
    return PIL.ImageGrab.grab().load()[location]

PPI = 100.7
CONTROL_LOCATION = (1 * PPI, 8 * PPI)
SHARE_LOCATION = (1.5 * PPI, 5.75 * PPI)
HOME_LOCATION = (0.5 * PPI, 0.75 * PPI)
UPLOAD_LOCATION = (6 * PPI, 0.75 * PPI)
YELLOW_LOCATION = (10 * PPI, 4.5 * PPI)
GREY_BACK_LOCATION = (3 * PPI, 2.5 * PPI)

SHARE_NOT_TOGGLED_COLOR = (228, 231, 233)
YELLOW_COLOR = (247, 245, 226)
GREY_COLOR = (123, 123, 123)

with open("target_dir.txt", 'r') as f:
    path = f.read().strip("'")

files = os.listdir(path)

print(files)

for file in files:
    print(file)
    pyautogui.hotkey('ctrl', 'o', interval = 0.15)
    time.sleep(1)
    pyperclip.copy(file.strip("'"))
    pyautogui.hotkey('enter')
    
    while (get_color(GREY_BACK_LOCATION) == GREY_COLOR):
        print("waiting to open")
        time.sleep(1)

    pyautogui.click(CONTROL_LOCATION) 
    if (get_color(SHARE_LOCATION) == SHARE_NOT_TOGGLED_COLOR):
        pyautogui.click(SHARE_LOCATION)
        time.sleep(0.3)
        pyautogui.click((SHARE_LOCATION[0], SHARE_LOCATION[1] + 50))
        time.sleep(0.3)
        pyautogui.click(UPLOAD_LOCATION)
        time.sleep(0.3)
        pyautogui.hotkey('enter')
       
        while (get_color(YELLOW_LOCATION) != YELLOW_COLOR):
            print("waiting to upload")
            time.sleep(1) 
            
        pyautogui.hotkey('esc')
        time.sleep(0.3)
        pyautogui.click(HOME_LOCATION)
        continue
    else: 
        pyautogui.click(HOME_LOCATION)
        continue

time.sleep(10)