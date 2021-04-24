from win32_connectors import KeyboardConnectors

import time
from tft import ProcessChecker
from pynput.keyboard import Key, Controller
from win32_connectors.KeyboardConnectors import ESC
from win32_connectors.MouseConnectors import Mouse

ACCEPTBUTTON = (958, 716)
FINDMATCH = (855, 839)
PLAYAGAIN = (855, 843)
COLLECTREWARDS = (960, 840)

FFBUTTON = (760, 870)
CONFIRMBUTTON = (855, 605)
EXITNOW = (830,530)

SLEEPTIMER = 0.3
WAITTIMER = 0.1
TIMEUNTILFF = 900
DEACTIVATIONTIMER = 60


def mouseclick(mouse, button, coords):
    time.sleep(SLEEPTIMER)
    mouse.move_mouse(coords)
    time.sleep(SLEEPTIMER)
    if button:
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

# 1866
if __name__ == "__main__":
    mouse = Mouse()
    alttab()

    for i in range(200):
        # get into game
        # get into q
        continued = True
        mouseclick(mouse, True, FINDMATCH)
        while ProcessChecker.CheckforLeague() is False:
            mouseclick(mouse, True, ACCEPTBUTTON)
            time.sleep(2)
        print("got into game....")
        print("waiting " + str(TIMEUNTILFF) + " until FF")
        time.sleep(60)
        mouseclick(mouse, True, ACCEPTBUTTON)
        time.sleep(TIMEUNTILFF)
        while ProcessChecker.CheckforLeague():
            mouseclick(mouse, True, EXITNOW)
            #surrender(mouse)
            print("trying to click exit now")
            time.sleep(45)
        print("game finished")
        for n in range(4):
            mouseclick(mouse, True, COLLECTREWARDS)
            time.sleep(2)
        mouseclick(mouse, True, PLAYAGAIN)
        time.sleep(DEACTIVATIONTIMER)

# time to stop this process

# find match
# time delay / screenshot
#

# start sequence

# click find match
# while not ingame
# press accept

# once ingame
# wait 10/14mins??????

# do surrender
# esc
# surrender
# yes

# postgame

# accept
