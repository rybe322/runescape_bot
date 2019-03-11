import os
import time

import pyautogui

INTERVAL = 0.25
CLICKS = 1
# Gets the corners of a window
# TLC, TRC, BLC, BRC
def get_files(file_path = "") :
    files = os.listdir(file_path)
    return list(files)
def click_drop() :
    drop_button = './screenshots/inventory/misc/drop.png'
    drop_coord = pyautogui.locateOnScreen(drop_button, confidence=0.5)
    pyautogui.click(pyautogui.center(drop_coord)[0], pyautogui.center(drop_coord)[1])

def empty_inventory(item_type="copper") :
    print("\nempty_inventoryy begin")
    file_path = './screenshots/inventory/actions/'+item_type+'/'
    print("\n",file_path,"\n")
    drop_item = file_path+item_type+'_i.png'
    drop_button = file_path+item_type+'_d.png'
    try:
        drop_items = pyautogui.locateAllOnScreen(drop_item, confidence=0.7)
        for item in drop_items :
            print("\nitem:  ",item,"\n")
            print("\ndrop item:  ", drop_item, "\n")
            try:
                center = pyautogui.center(item)
                pyautogui.click(center[0], center[1], button='right')
                drop_button = './screenshots/inventory/misc/drop.png'
                drop_coord = pyautogui.locateOnScreen(drop_button, confidence=0.5)
                pyautogui.click(pyautogui.center(drop_coord)[0], pyautogui.center(drop_coord)[1])
                #click_drop()
                '''
                drop_center = pyautogui.center(pyautogui.locateOnScreen(drop_item, confidence=0.5))
                pyautogui.moveTo(drop_center[0], drop_center[1], interval = 10)
                pyautogui.click(drop_center[0], drop_center[1])
                #button = pyautogui.locateOnScreen(drop_button, confidence=0.50)
                '''
            except:
                continue
    except:
        return

def mining(file_path='', ore_type="") :
    files = get_files(file_path)

    inv_full = './screenshots/inv_full.png'
    for name in files :
        if(inventory_full()) :
            print("main_inv_if")
            empty_inventory(ore_type)
        print(name)
        try:
            print("\ntry\n")
            x,y = pyautogui.locateCenterOnScreen(file_path+name, confidence=0.6)
            #pyautogui.click(x, y)
            pyautogui.click(x, y, clicks = CLICKS, interval=INTERVAL)
            print(x,y)
        except :
            print("\nexcept\n")

def inventory_full() :
    full_file = './screenshots/inventory/misc/full.png'
    try :
        print("\ntry inv full\n")
        pyautogui.locateOnScreen(full_file, confidence=0.5)
        return True
    except :
        print("\nexcept inv full\n")
        return False

if __name__ == '__main__':
    print('Press Ctrl-C to quit.')
    try:
        while(True) :
            #file_path = './screenshots/mining/copper/'
            file_path = './screenshots/mining/coal/'
            files = get_files(file_path)
            #get_good_screen_shots(files, file_path)
            #mining(file_path, ore_type="copper")
            mining(file_path, ore_type="coal")

    except KeyboardInterrupt :
        print("\nDone.")
        exit(1)
