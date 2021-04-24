import psutil

def CheckforLeague():
    var = "League of Legends.exe" in (p.name() for p in psutil.process_iter())
    return var

def Debugfunction():
    for prog in psutil.process_iter():
        if prog.name().__contains__("League"):
            print(prog.name())

#print(CheckforLeague())