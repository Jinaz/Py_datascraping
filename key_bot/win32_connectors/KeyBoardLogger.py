from win32api import GetKeyState

# Our Definitions
def keyIsUp(key):
    keystate = GetKeyState(key)
    if (keystate == 0) or (keystate == 1):
        return True
    else:
        return False


def keyIsDown(key):
    keystate = GetKeyState(key)
    if (keystate != 0) and (keystate != 1):
        return True
    else:
        return False