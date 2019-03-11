import time

import pyautogui

# Gets the corners of a window
# TLC, TRC, BLC, BRC
P_LENGTH = 200000000000
def get_corners() :
        corner_dict = {}
        print("Move to top left corner\n")
        x, y = pyautogui.position()
        pyautogui.PAUSE = P_LENGTH
        corner_dict['tlc'] = (x,y)
        print("\nx:  ", x, "\ny:  ", y)
        print("Move to top right corner\n")
        pyautogui.PAUSE = P_LENGTH
        x, y = pyautogui.position()
        corner_dict['tlc'] = (x,y)
        print("\nx:  ", x, "\ny:  ", y)
        return corner_dict
        return corner_dict



if __name__ == '__main__':
    print('Press Ctrl-C to quit.')
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
