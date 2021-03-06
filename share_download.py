import pyperclip
import time
import pyautogui
import PIL.ImageGrab
import os
import smtplib

def get_color(location):
    return PIL.ImageGrab.grab().load()[location]

PPI = 100.7
CONTROL_LOCATION = (175, 750)
SHARE_LOCATION = (138, 542)
PRINT_LOCATION = (138, 585)
HOME_LOCATION = (50, 67)
UPLOAD_LOCATION = (560, 65)
YELLOW_LOCATION = (1205, 411)
GREY_LOCATION = (915, 478)

NOT_TOGGLED_COLOR = (228, 231, 233)
YELLOW_COLOR = (247, 245, 226)

with open("target_dir.txt", 'r') as f:
    path = f.read().strip("'")

files = os.listdir(path)

print(files)

for file in files:
    print(file)
    pyautogui.click(86, 288)
    pyperclip.copy(file.strip("'"))
    pyautogui.hotkey('ctrl', 'o', interval = 0.15)
    time.sleep(0.3)
    pyautogui.hotkey('ctrl', 'v', interval = 0.15)
    time.sleep(0.3)
    pyautogui.hotkey('enter')
    
    time.sleep(1)

    while (get_color(GREY_LOCATION) == (97, 98, 99)):
        print("waiting to open")
        time.sleep(3)

    pyautogui.click(CONTROL_LOCATION) 
    time.sleep(2)

    if (get_color(SHARE_LOCATION) != NOT_TOGGLED_COLOR):
        pyautogui.click(SHARE_LOCATION)
        share_flag = True
        time.sleep(0.3)

    if (get_color(PRINT_LOCATION) != NOT_TOGGLED_COLOR):
        pyautogui.click(PRINT_LOCATION)
        print_flag = True
        time.sleep(0.3)

    if (share_flag or print_flag):
        pyautogui.click(UPLOAD_LOCATION)
        time.sleep(0.3)
        pyautogui.hotkey('enter')

        start_time = time.time()
        while (get_color(YELLOW_LOCATION) != YELLOW_COLOR):
            if (time.time() - start_time > 600):
                print("***************\n \n \n \n \n {} FAILED \n \n \n \n \n \n*************".format(file))
                continue
            print("waiting to upload")
            time.sleep(3) 
    
    share_flag = False
    print_flag = False

    pyautogui.hotkey('esc')
    time.sleep(1)
    pyautogui.click(HOME_LOCATION)
    time.sleep(0.5)
