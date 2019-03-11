import os
import pyautogui as pag
import sys
pag.PAUSE=3
pag.FAILSAFE=True

def get_click_list(clicks = 2) :
    l = []
    for i in range(clicks):
        a = input("Hover over spot and press enter...")
        l.append(pag.position())
        print(pag.position())

    return l

def doc_example() :
    print('Press Ctrl-C to quit.')
    try:
        while True:
            x, y = pag.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print(positionStr, end='')
            print('\b' * len(positionStr), end='', flush=True)
    except KeyboardInterrupt:
        print('\n')


def find_on_screen(fh="", conf=0.5) :
    try:
        return pag.locateOnScreen(fh, confidence=conf)
    except:
        print("Did not find cow!\n",fh,"-fh")
        return False
def find_cow(fh="", conf=0.5) :
    try:
        return pag.locateOnScreen(fh, confidence=conf)
        print("found cow!\n",fh,"-fh")
    except:
        print("Did find cow!\n",fh,"-fh")
        return False

def cows() :
    cows = ['./cows/'+x for x in os.listdir('./cows/')]
    for cow in cows :
        try:
            for coord in find_cow(cow):
                cent = pag.center(coord)
                pag.click(cent[0], cent[1])
        except KeyboardInterrupt:
            exit(1)
        except:
            print("except")
            continue

def get_files(path="", ret_path=True):
    return([path+f for f in os.listdir(path)])

def get_center(fh="", conf=0.7):
    try:
        coord = pag.locateOnScreen(fh, confidence=conf)
        return(pag.center(coord))
    except:
        pass

def mine(path='./coal_/', conf=0.6):
    for coal in get_files(path):
        try:
            print(coal)
            x,y=pag.locateCenterOnScreen(coal, confidence=conf)
            print(x,y)
            pag.click(x,y)
        except:
            continue
def bank_chest(path="./coal_/bank_chest/bank_chest/"):

    for chest in get_files(path):
    #bank_chest = path+'bank_chest.png'
        try:
            x,y = pag.locateCenterOnScreen(chest, confidence=0.7)
            pag.click(x,y)
        except:
            continue
def deposit_ore(path="./coal_/bank_chest/"):
    deposit_all = path+'deposit_all.png'
    try:
        deposit_all_button = pag.locateCenterOnScreen(deposit_all, confidence=0.8)
        pag.click(deposit_all_button[0], deposit_all_button[1])
        close_bank_window = pag.locateCenterOnScreen(path+'bank_inventory_x_button.png',confidence=0.7)
        pag.click(close_bank_window[0], close_bank_window[1])
    except:
        pass


#def bank_window_open(path="./coal_/"):

def full(path='./coal_/bank_chest/'):
    full=path+'full.png'
    try:
        x,y = pag.locateCenterOnScreen(full,confidence=0.7)
        return(True)
    except:
        return(False)

def good():
    if(not full()):
        mine()
        return True
    else:
        bank_chest()
        deposit_ore()
    good()
def not_good():
    bank_chest()
    deposit_ore()
