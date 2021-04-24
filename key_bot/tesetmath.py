
import win32_connectors.MouseConnectors as mc
from win32gui import GetWindowText, GetForegroundWindow
import time
from pynput.keyboard import Key, Controller, Listener

keyboard = Controller()
m = mc.Mouse()

hppoints = 6
stampoints = 0
meleepoints = 60

def on_press(key):
    #print(key , "pressed")
    pass
def on_re_lease(key):
    if key == Key.ctrl_r:

        for i in range(20):
            keyboard.press(Key.tab)
            time.sleep(0.1)
            keyboard.release(Key.tab)
            time.sleep(0.1)

            keyboard.press(Key.up)
            time.sleep(0.1)
            keyboard.release(Key.up)
            time.sleep(0.1)
            keyboard.press(Key.up)
            time.sleep(0.1)
            keyboard.release(Key.up)
            time.sleep(0.1)
            keyboard.press(Key.enter)
            time.sleep(0.1)
            keyboard.release(Key.enter)
            time.sleep(0.5)

            keyboard.press(Key.tab)
            time.sleep(0.1)
            keyboard.release(Key.tab)
            time.sleep(0.1)

            keyboard.press(Key.up)
            time.sleep(0.1)
            keyboard.release(Key.up)
            time.sleep(0.1)
            keyboard.press(Key.up)
            time.sleep(0.1)
            keyboard.release(Key.up)
            time.sleep(0.1)
            keyboard.press(Key.enter)
            time.sleep(0.1)
            keyboard.release(Key.enter)
            time.sleep(0.5)

            m.press_button((-1, -1), "left")
            time.sleep(0.1)
            m.press_button((-1, -1), "left", True)
            time.sleep(0.1)

def on_release(key):
    if key == Key.alt_l:
        #keyboard.press(Key.alt)
        #time.sleep(0.1)
        #keyboard.press(Key.tab)

        #time.sleep(0.1)

        #keyboard.release(Key.tab)
        #time.sleep(0.1)
        #keyboard.release(Key.alt)
        #time.sleep(0.4)





        # health
        for i in range(hppoints):
            m.press_button((1120, 500), "left")
            time.sleep(0.1)
            m.press_button((1120, 500), "left", True)
            time.sleep(0.01)
        # stamina
        for i in range(stampoints):
            m.press_button((1120, 536), "left")
            time.sleep(0.1)
            m.press_button((1120, 536), "left", True)
            time.sleep(0.01)
        # melee
        for i in range(meleepoints):
            m.press_button((1120, 679), "left")
            time.sleep(0.1)
            m.press_button((1120, 679), "left", True)
            time.sleep(0.01)

        keyboard.press(Key.esc)
        time.sleep(0.1)
        keyboard.release(Key.esc)


current_window = (GetWindowText(GetForegroundWindow()))
desired_window_name = "ARK: Survival Evolved" #Whatever the name of your window should be

#print(GetWindowText(GetForegroundWindow()))
try:
    while True:
        #print(GetWindowText(GetForegroundWindow()))
        if current_window == desired_window_name:
            with Listener(
                    on_press=on_press,
                    on_release=on_release) as listener:
                listener.join()

        current_window = (GetWindowText(GetForegroundWindow()))


except KeyboardInterrupt:
    pass


