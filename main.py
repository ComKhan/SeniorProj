'''
Senior Project
Humming Bluetooth Synthesizer
main.py
'''
from multiprocessing.pool import INIT
#import buttons
import time

'''
# imports for usb audio
import pyaudio
import matplotlib.pyplot as plt
import numpy as np
import wave
'''
# imports for buttons.py
import RPi.GPIO as GPIO
from gpiozero import Button

# Import local py files
import rootFSM as fsm
import btns

'''
global variables


'''

''' Using fsm code
States

'''


class currProps(object): # stores current values for FSM
    def __init__(self):
        self.currState = INIT


current = currProps()

##================================================================================

#recordVal = buttons.btnClk() # instance of settings for the record button
#recordVal.clicked()


# method in video, using Char method
inFSM = True # stays in FSM while true

if __name__ == "__main__":
    mainFSM = fsm.Char() # create an instance of the FSM
    
    # add states instances
    mainFSM.FSM.states["InitS"] = fsm.InitS() #instance of Set state stored within state dictionary inside FSM
    mainFSM.FSM.states["WaitS"] = fsm.WaitS()
    mainFSM.FSM.transitions["toWaitS"] = fsm.Transition("WaitS") # create instance of those transitions and store them within trans dictionary
    mainFSM.FSM.transitions["toInitS"] = fsm.Transition("InitS")
    
    #set initial state
    mainFSM.FSM.SetState("InitS")

    print("enter main now")
    while inFSM:
        match mainFSM.FSM.curStateName:
            case "InitS":
                btns.btn1.when_pressed = btns.clickA.clicked()
                # Testing code: Remove for full implementation
                #lcd.write_lcd("Synth Start    F", "A B C D E      G") # add when import lcd
                print("Synth Start    F")
                #mainFSM.FSM.Transition("toWaitS")
                time.sleep(5)
                # End Testing Code

                pass

            case "WaitS": 
                # button presses will cause transitions to other states
                btns.btn1.when_pressed = btns.clickA.clicked()
                btns.btn2.when_pressed = btns.clickB.clicked()
                btns.btn3.when_pressed = btns.clickC.clicked()
                btns.btn4.when_pressed = btns.clickD.clicked()
                btns.btn5.when_pressed = btns.clickE.clicked()
                btns.btn6.when_pressed = btns.clickF.clicked()
                btns.btn7.when_pressed = btns.clickG.clicked()

                # Testing code: Remove for full implementation
                mainFSM.FSM.Transition("toInitS")
                mainFSM.FSM.curStateName = "InitS"
                print("State 2")
                time.sleep(5)
                # End Testing Code

                pass

            case "RecordS":

                pass

            case "StoreS":

                pass
            
            case "PlayS":

                pass

            case "QuickVol":

                pass

            case "SetVolS":

                pass
                
            case "SetInstS":

                pass

            case "SetFilterS":

                pass

            case "SetOutS":

                pass   

            case _:

                pass

        mainFSM.FSM.Go()
        pass