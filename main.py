'''
Senior Project
Humming Bluetooth Synthesizer
main.py
'''
# imports for buttons.py
import RPi.GPIO as GPIO
from gpiozero import Button


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
#global btn1, btn2, btn3, btn4, btn5, btn6, btn7

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
        testName = mainFSM.FSM.curStateName
        testTrans = mainFSM.FSM.trans
        if testTrans == None:
            #print("trans == None")
            mainFSM.FSM.Go()
            if btns.clickA.implement == False: # set up for each button
                print("state A clicked button")
                mainFSM.FSM.Transition("toWaitS")
                testTrans = mainFSM.FSM.trans
                btns.clickA.implement = True
            #print("go")
            if btns.clickB.implement == False: # set up for each button
                print("state B clicked button")
                mainFSM.FSM.Transition("toInitS")
                testTrans = mainFSM.FSM.trans
                btns.clickB.implement = True
        

        else:
            #print("edge case FAIL")
            mainFSM.FSM.Transition(mainFSM.FSM.transName)
            mainFSM.FSM.Go()

        
        pass
    
## working fsm but messy, make sure to add Go() after all cases
'''if testName == "InitS": 
            btn1.when_pressed = btns.clickA.clicked
            if btn1.is_pressed:
                btns.clickA.clicked()
                print("state A clicked button")
            if btns.clickA.implement == False:
                print("state A clicked button")
                mainFSM.FSM.Transition("toWaitS")
                btns.clickA.implement = True
            # Testing code: Remove for full implementation
            #lcd.write_lcd("Synth Start    F", "A B C D E      G") # add when import lcd
            #print("Synth Start    F")
            #mainFSM.FSM.Transition("toWaitS")
            #time.sleep(5)
            # End Testing Code

            pass

        elif testName == "WaitS": 
            # button presses will cause transitions to other states
            #btn1.when_pressed = btns.clickA.clicked
            btns.btn2.when_pressed = btns.clickB.clicked()
            btns.btn3.when_pressed = btns.clickC.clicked()
            btns.btn4.when_pressed = btns.clickD.clicked()
            btns.btn5.when_pressed = btns.clickE.clicked()
            btns.btn6.when_pressed = btns.clickF.clicked()
            btns.btn7.when_pressed = btns.clickG.clicked()

            # Testing code: Remove for full implementation
            #mainFSM.FSM.Transition("toInitS")
            #mainFSM.FSM.curStateName = "InitS"
            print("State 2")
            time.sleep(5)
            # End Testing Code

            pass'''

'''case "RecordS":

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

        pass'''   
