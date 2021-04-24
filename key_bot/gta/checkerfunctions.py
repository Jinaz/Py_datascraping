import psutil
import time

def show_all_Processes():
    for p in psutil.process_iter():
        print(p.name)


def checkForGTA():
    while("GTA5.exe" in (p.name() for p in psutil.process_iter())):
        print("GTA5 is running")
        time.sleep(5)
    print("GTAV is not running")

