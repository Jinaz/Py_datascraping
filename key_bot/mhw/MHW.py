from pynput.keyboard import Key, Controller
import time

from win32_connectors.KeyboardConnectors import PressKey, ReleaseKey, A,S,D,N,E

sleeptimer = 0.1
waittimer = 0.1

def goRight(times):
    for i in range(times):
        PressKey(D)
        time.sleep(sleeptimer)
        ReleaseKey(D)
        time.sleep(waittimer)

def goLeft(times):
    for i in range(times):
        PressKey(A)
        time.sleep(sleeptimer)
        ReleaseKey(A)
        time.sleep(waittimer)

def pressE():
    PressKey(E)
    time.sleep(sleeptimer)
    ReleaseKey(E)
    time.sleep(waittimer)

def goDown():
    PressKey(S)
    time.sleep(sleeptimer)
    ReleaseKey(S)
    time.sleep(waittimer)

def pressN():
    PressKey(N)
    time.sleep(sleeptimer)
    ReleaseKey(N)
    time.sleep(waittimer)

def outerfunction():
    for x in range(10):
        pressN()
        goRight(x)
        pressN()
        goLeft(x)

def initfuncction():
    for out in range(1):

        for c in range(5):
            outerfunction()
            goDown()
        pressN()
        pressE()



keyboard = Controller()

time.sleep(1)

keyboard.press(Key.alt)
time.sleep(0.1)
keyboard.press(Key.tab)

time.sleep(0.1)

keyboard.release(Key.tab)
time.sleep(0.1)
keyboard.release(Key.alt)

time.sleep(2)
initfuncction()

time.sleep(3)
print("We are done")