import pyperclip
import time
import pyautogui
import PIL.ImageGrab
import os

def get_color(location):
    return PIL.ImageGrab.grab().load()[location]

PPI = 100.7
CONTROL_LOCATION = (175, 750)
SHARE_LOCATION = (138, 542)
PRINT_LOCATION = (138, 585)
HOME_LOCATION = (50, 67)
UPLOAD_LOCATION = (560, 65)
YELLOW_LOCATION = (1205, 411)
GREY_BACK_LOCATION = (250, 300)

SHARE_NOT_TOGGLED_COLOR = (228, 231, 233)
YELLOW_COLOR = (247, 245, 226)
GREY_COLOR = (124, 124, 124)

with open("target_dir.txt", 'r') as f:
    path = f.read().strip("'")

files = os.listdir(path)

print(files)

for file in files:
    print(file)
    pyautogui.click(86, 288)
    pyperclip.copy(file.strip("'"))
    pyautogui.hotkey('ctrl', 'o', interval = 0.15)
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'v', interval = 0.15)
    time.sleep(2)
    pyautogui.hotkey('enter')
    
    while (get_color(GREY_BACK_LOCATION) == GREY_COLOR):
        print("waiting to open")
        time.sleep(3)

    pyautogui.click(CONTROL_LOCATION) 
    
    if (get_color(SHARE_LOCATION) != SHARE_NOT_TOGGLED_COLOR):
        pyautogui.click(SHARE_LOCATION)
        time.sleep(0.3)
        pyautogui.click(PRINT_LOCATION)
        time.sleep(0.3)
        pyautogui.click(UPLOAD_LOCATION)
        time.sleep(0.3)
        pyautogui.hotkey('enter')
       
        while (get_color(YELLOW_LOCATION) != YELLOW_COLOR):
            print("waiting to upload")
            time.sleep(3) 
            
        pyautogui.hotkey('esc')
        time.sleep(0.3)
        pyautogui.click(HOME_LOCATION)
        continue
    else: 
        pyautogui.click(HOME_LOCATION)
        continue

time.sleep(100)