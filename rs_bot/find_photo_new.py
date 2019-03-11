import os
import time

import pyautogui

INTERVAL = 1.5
CLICKS = 10
# Gets the corners of a window
# TLC, TRC, BLC, BRC
def get_files(file_path = "") :
    files = os.listdir(file_path)
    return list(files)
def empty_inventory(file_path="") :
    drop_ore = './screenshots/inv_iron.png'
    drop_button = './screenshots/drop_button_tin.png'
    drop_items = pyautogui.locateAllOnScreen(drop_ore, confidence=0.5)
    for item in drop_items :
        try:
            center = pyautogui.center(item)
            pyautogui.click(center[0], center[1], button='right')
            button = pyautogui.locateOnScreen(drop_button, confidence=0.50)
            pyautogui.click(pyautogui.center(button)[0], pyautogui.center(button)[1])
        except:
            continue
def get_good_screen_shots(files, file_path='') :

    inv_full = './screenshots/inv_full.png'
    for name in files :
        print(name)
        try:
            print("\ntry\n")
            x,y = pyautogui.locateCenterOnScreen(file_path+name, confidence=0.6)
            #pyautogui.click(x, y)
            pyautogui.click(x, y, clicks = CLICKS, interval=INTERVAL)
            iron_x, iron_y = pyautogui.locateCenterOnScreen(file_path+'inv_iron.png', confidence=0.5)
            pyautogui.moveTo(iron_x, iron_y, 10)
            print(x,y)
            time.sleep(30)
        except :
            print("\nexcept\n")

if __name__ == '__main__':
    print('Press Ctrl-C to quit.')
    try:
        while(True) :
            file_path = './screenshots/iron/'
            files = get_files(file_path)
            get_good_screen_shots(files, file_path)
            try:
                inventory_full = pyautogui.locateOnScreen('./screenshots/inv_full.png',confidence=0.5)
                if(inventory_full) :
                    print("\nInventory full...\n")
                    empty_inventory()
            except :
                continue

    except KeyboardInterrupt :
        print("\nDone.")
        exit(1)
    '''
    try:
        get_corners()
        while True:
            # Get and print the mouse coordinates.
            x, y = pyautogui.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print("\r", positionStr, end="", flush=True)
            print("TOP LEFT CORNER\n")
            time.sleep(5)
            x, y = pyautogui.position()
            tlcx = x
            tlcy = y
            print("tlcx:  ", tlcx, " tlcy:  " , tlcy)

    except KeyboardInterrupt:
        print('\nDone.')
'''
