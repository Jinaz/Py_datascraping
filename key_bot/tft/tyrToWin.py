from win32_connectors import KeyboardConnectors

import time
from tft import ProcessChecker
import old_code_fragments.detectAndBuy as cvf
from pynput.keyboard import Key, Controller
from win32_connectors.KeyboardConnectors import ESC
from win32_connectors.MouseConnectors import Mouse
from datetime import timedelta
import random

ACCEPTBUTTON = (958, 716)
FINDMATCH = (855, 839)
PLAYAGAIN = (855, 843)
COLLECTREWARDS = (960, 840)

CHAMPS = [(580, 990), (780, 990), (980, 990), (1180, 990), (1380, 990)]
CHAMP1 = (580, 990)
CHAMP2 = (780, 990)
CHAMP3 = (980, 990)
CHAMP4 = (1180, 990)
CHAMP5 = (1380, 990)

UPGRADE = (367, 960)
REFRESH = (367, 1040)

FFBUTTON = (760, 870)
CONFIRMBUTTON = (855, 605)
EXITNOW = (830,530)

SLEEPTIMER = 0.3
WAITTIMER = 0.1
TIMEUNTILFF = 780
DEACTIVATIONTIMER = 60

#true left click
#false right click
#function to simulate a click
def mouseclick(mouse, leftbutton, coords):
    time.sleep(SLEEPTIMER)
    mouse.move_mouse(coords)
    time.sleep(SLEEPTIMER)
    if leftbutton:
        mouse.press_button(mouse.get_position(), "left", False)
        time.sleep(WAITTIMER)
        mouse.press_button(mouse.get_position(), "left", True)
    else:
        mouse.press_button(mouse.get_position(), "right", False)
        time.sleep(WAITTIMER)
        mouse.press_button(mouse.get_position(), "right", True)
    time.sleep(SLEEPTIMER)


def alttab():
    keyboard = Controller()

    time.sleep(1)

    keyboard.press(Key.alt)
    time.sleep(0.1)
    keyboard.press(Key.tab)

    time.sleep(0.1)

    keyboard.release(Key.tab)
    time.sleep(0.1)
    keyboard.release(Key.alt)
    time.sleep(1)


def smt():
    mouse = Mouse()
    # mouse.click((100, 100), "right")
    mouse.move_mouse((100, 100))
    mouse.click()
    mouse.move_mouse((200, 200))
    time.sleep(1)
    mouse.press_button(mouse.get_position(), "right", False)
    time.sleep(1)
    mouse.press_button(mouse.get_position(), "right", True)
    # time.sleep(2.0)

    # mouse.click((100, 100), "right")


def pressEsc():
    time.sleep(SLEEPTIMER)
    KeyboardConnectors.PressKey(ESC)
    time.sleep(WAITTIMER)
    KeyboardConnectors.ReleaseKey(ESC)
    time.sleep(SLEEPTIMER)


def surrender(mouse):
    # ff sequence after waiting
    pressEsc()
    # true left else right
    mouseclick(mouse, True, FFBUTTON)
    mouseclick(mouse, True, CONFIRMBUTTON)

#2142
if __name__ == "__main__":
    mouse = Mouse()
    alttab()
    rebel = cvf.load_class('rebel')

    for i in range(20):
        # get into game
        # get into q
        #continued = True
        mouseclick(mouse, True, FINDMATCH)
        while ProcessChecker.CheckforLeague() is False:
            mouseclick(mouse, True, ACCEPTBUTTON)
            time.sleep(2)

        print("got into game....")
        # wait for loading screen and focus to game
        start_time = time.time()
        mouseclick(mouse, True, ACCEPTBUTTON)

        # try to exit
        while ProcessChecker.CheckforLeague():
            champs = cvf.get_index(rebel)

            if len(champs) > 0:
                print('buying champ...')
                for i in champs:
                    mouseclick(mouse, True, CHAMPS[i])
            else:
                print('no rebel champs')

            if time.time() - start_time > TIMEUNTILFF:
                mouseclick(mouse, True, UPGRADE)

                if random.randint(0, 9) >= 5:
                    mouseclick(mouse, True, UPGRADE)

                mouseclick(mouse, True, EXITNOW)
                print("trying to click exit now")

            time.sleep(30)

        print("game finished")
        print("game time: ", str(timedelta(seconds=(time.time() - start_time))))

        # restart game
        for n in range(4):
            mouseclick(mouse, True, COLLECTREWARDS)
            time.sleep(2)
        mouseclick(mouse, True, PLAYAGAIN)
        time.sleep(DEACTIVATIONTIMER)

