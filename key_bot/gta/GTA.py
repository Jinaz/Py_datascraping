# move in circle
# check for lobby screen
# check after game
# pytess
# ocv
# keyboard
# mouse
import win32_connectors.KeyboardConnectors as kc
import time
import imageFunctions.imagecomparison as ic
from enum import Enum

from win32_connectors.KeyBoardLogger import keyIsUp


class State(Enum):
    VOTING = 1
    MENU = 2
    INGAME = 3
    STARTED = 4
    NULL = 5

def movement_WA():
    kc.PressKey(kc.W)
    kc.PressKey(kc.A)
    time.sleep(1.2)
    kc.ReleaseKey(kc.W)
    kc.ReleaseKey(kc.A)


def movement_SD():
    kc.PressKey(kc.S)
    kc.PressKey(kc.D)
    time.sleep(1)
    kc.ReleaseKey(kc.S)
    kc.ReleaseKey(kc.D)





menuCoords = [118, 155, 304, 405]
votemenuCoords = [108, 155, 308, 615]
PrepareInGame = [1033, 1064, 772, 1148]
MissionInGame = [1030, 1069, 797, 1121]
threshold = 0.94

def loadTemplates():
    import cv2 as cv
    enemyTemplate = cv.imread("DATA/enemyFiltered.png",cv.IMREAD_GRAYSCALE)
    menuTemplate = cv.imread("DATA/menuFiltered.png",cv.IMREAD_GRAYSCALE)
    postTemplate = cv.imread("DATA/postFiltered.png",cv.IMREAD_GRAYSCALE)
    prepTemplate = cv.imread("DATA/prepFiltered.png",cv.IMREAD_GRAYSCALE)

    #enemyTemplate = ic.prefilter(enemyTemplate, "thresh")
    #menuTemplate = ic.prefilter(menuTemplate, "thresh")
    #postTemplate = ic.prefilter(postTemplate, "thresh")
    #prepTemplate = ic.prefilter(prepTemplate, "thresh")

    return enemyTemplate, menuTemplate, postTemplate, prepTemplate


def get_data():
    im = ic.screenshotToData()
    menu = im[menuCoords[0]:menuCoords[1], menuCoords[2]:menuCoords[3], :]
    vote = im[votemenuCoords[0]:votemenuCoords[1], votemenuCoords[2]:votemenuCoords[3], :]
    prep = im[PrepareInGame[0]:PrepareInGame[1], PrepareInGame[2]:PrepareInGame[3], :]
    miss = im[MissionInGame[0]:MissionInGame[1], MissionInGame[2]:MissionInGame[3], :]

    menu = ic.prefilter(menu, "opening")
    vote = ic.prefilter(vote, "opening")
    prep = ic.prefilter(prep, "opening")
    miss = ic.prefilter(miss, "opening")

    return menu, vote, prep, miss

def check_in_menu(menu, menuTemplate):
    x = ic.compare_CV_images(menuTemplate, menu)
    if x[1] > threshold:
        print("in menu")
        #print(x)
        return True
    return False

def check_gameStatus(prep,enemy, prepTemplate, enemyTemplate):
    z = ic.compare_CV_images(prep, prepTemplate)
    if z[1] > threshold:
        print("preparing")
        #print(z)
        return 1
    w = ic.compare_CV_images(enemy, enemyTemplate)
    if w[1] > threshold:
        print("enemy")
        #print(w)
        return 2
    return 0

def checkVoting(vote, voteTemplate):
    y = ic.compare_CV_images(vote, voteTemplate)
    if y[1] > threshold:
        print("voting")
        #print(y)
        return True
    return False

def doVote():
    kc.PressKey(kc.S)
    time.sleep(.1)
    kc.ReleaseKey(kc.S)
    time.sleep(.8)
    kc.PressKey(kc.S)
    time.sleep(.1)
    kc.ReleaseKey(kc.S)
    time.sleep(.8)
    kc.PressKey(kc.ENTER)
    time.sleep(.2)
    kc.ReleaseKey(kc.ENTER)
    time.sleep(.2)

def afkTime(vote, voteTemplate):
    # check for voting

    sleeptime = 2
    voting = checkVoting(vote, voteTemplate)
    if voting:
        sleeptime = 0
    time.sleep(sleeptime)
    menu, vote, prep, miss = get_data()
    if checkVoting(vote, voteTemplate):
        doVote()
        return State.VOTING, True
    return State.INGAME, False
    # check for voting

def startMission():
    kc.PressKey(kc.W)
    time.sleep(.1)
    kc.ReleaseKey(kc.W)
    time.sleep(.2)
    kc.PressKey(kc.ENTER)
    time.sleep(.1)
    kc.ReleaseKey(kc.ENTER)
    time.sleep(.2)

def alttab():
    kc.PressKey(kc.ALT)
    kc.PressKey(kc.TAB)
    time.sleep(.2)
    kc.ReleaseKey(kc.TAB)
    kc.ReleaseKey(kc.ALT)
    time.sleep(.2)

def ingameDone():
    alttab()
    voted = False
    startMission()
    currentState = State.INGAME
    currentwave = 0
    while keyIsUp(81):

        enemyTemplate, menuTemplate, postTemplate, prepTemplate = loadTemplates()
        menu, vote, prep, miss = get_data()

        # check menu
        if currentState == State.INGAME:

            menu, vote, prep, miss = get_data()
            state = check_gameStatus(prep, miss, prepTemplate, enemyTemplate)
            if state == 1:
                movement_WA()
                menu, vote, prep, miss = get_data()
                if checkVoting(vote, voteTemplate=postTemplate):
                    doVote()
                    voted = True
            if state == 2:
                movement_SD()
                menu, vote, prep, miss = get_data()
                if checkVoting(vote, voteTemplate=postTemplate):
                    doVote()
                    voted = True
            if state == 0:
                menu, vote, prep, miss = get_data()
                if checkVoting(vote, voteTemplate=postTemplate):
                    doVote()
                    voted = True
            if not voted:
                menu, vote, prep, miss = get_data()
                currentState, voted = afkTime(vote, postTemplate)

        if voted:
            menu, vote, prep, miss = get_data()
            if check_in_menu(menu, menuTemplate):
                voted = False
                time.sleep(12)
                startMission()
                currentState = State.INGAME
        # up enter
        # status ingame

        # if ingame and null next is ingame or vote

        time.sleep(1)

def tempcode():
    alttab()
    enemyTemplate, menuTemplate, postTemplate, prepTemplate = loadTemplates()
    menu, vote, prep, miss = get_data()
    if check_in_menu(menu, menuTemplate):
        startMission()
    if checkVoting(vote, voteTemplate=postTemplate):
        doVote()

def debugcode():
    alttab()
    while keyIsUp(81):
        enemyTemplate, menuTemplate, postTemplate, prepTemplate = loadTemplates()
        menu, vote, prep, miss = get_data()
        if check_in_menu(menu, menuTemplate):
            time.sleep(15)

            startMission()
        if checkVoting(vote, postTemplate):
            doVote()

        time.sleep(2)
if __name__ == "__main__":
    ingameDone()



# prefilter the current screen
# compare to the templates


# if in menu do restart session
# else wa sd movement
