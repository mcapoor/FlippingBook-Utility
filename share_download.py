import pyperclip
import time
import pyautogui
import click
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

f = open('colors.txt', 'r')
SHARE_NOT_TOGGLED_COLOR, YELLOW_COLOR, GREY_COLOR = f.readlines()

files = os.listdir()

for file in files:
    pyautogui.hotkey('ctrl', 'o', interval = 0.15)
    pyperclip.copy(file.strip("'"))
    pyautogui.hotkey('enter')
    
    while (get_color(GREY_BACK_LOCATION) == GREY_COLOR):
        time.sleep(1)

    click.click(CONTROL_LOCATION) 
    if (get_color(SHARE_LOCATION) == SHARE_NOT_TOGGLED_COLOR):
        click.click(SHARE_LOCATION)
        click.clicK((SHARE_LOCATION[0], SHARE_LOCATION[1] + 50))
        click.click(UPLOAD_LOCATION)
        pyautogui.hotkey('enter')
       
        while (get_color(YELLOW_LOCATION) != YELLOW_COLOR):
            time.sleep(1) 
            
        pyautogui.hotkey('esc')
        click.click(HOME_LOCATION)
        continue
    else: 
        click.click(HOME_LOCATION)
        continue