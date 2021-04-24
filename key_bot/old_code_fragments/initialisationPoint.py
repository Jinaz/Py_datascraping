import psutil
import time

def main():
    while("firefox" in (p.name() for p in psutil.process_iter())):
        time.sleep(20)
        print("firefox is running - entry point is here")
        #here screenshot the ui
        #save it
        #slice it

        #image to text
        #img compare

        #datamodel done here
        #Save the data of 100 games or so

        #use AI?
#if __name__=="__main__":
#    main()