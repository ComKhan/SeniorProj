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
import rootFSM_V1 as fsm
import btns_V1

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
print("run")
if __name__ == "__main__":
    mainFSM = fsm.Char() # create an instance of the FSM
    print("go")
    # add states instances
    mainFSM.FSM.states["InitS"] = fsm.InitS() #instance of Set state stored within state dictionary inside FSM
    mainFSM.FSM.states["WaitS"] = fsm.WaitS()
    mainFSM.FSM.states["FilterS"] = fsm.FilterS()
    mainFSM.FSM.states["InstS"] = fsm.InstS()
    mainFSM.FSM.states["OutputS"] = fsm.OutputS()
    mainFSM.FSM.states["RecordS"] = fsm.RecordS()
    mainFSM.FSM.states["StoreS"] = fsm.StoreS()
    mainFSM.FSM.states["PlayS"] = fsm.PlayS()
    mainFSM.FSM.states["QuickVolS"] = fsm.QuickVolS()
    mainFSM.FSM.states["SetVolS"] = fsm.SetVolS()
    mainFSM.FSM.transitions["toWaitS"] = fsm.Transition("WaitS") # create instance of those transitions and store them within trans dictionary
    mainFSM.FSM.transitions["toInitS"] = fsm.Transition("InitS")
    mainFSM.FSM.transitions["toFilterS"] = fsm.Transition("FilterS")
    mainFSM.FSM.transitions["toInstS"] = fsm.Transition("InstS")
    mainFSM.FSM.transitions["toOutputS"] = fsm.Transition("OutputS")
    mainFSM.FSM.transitions["toRecordS"] = fsm.Transition("RecordS")
    mainFSM.FSM.transitions["toStoreS"] = fsm.Transition("StoreS")
    mainFSM.FSM.transitions["toPlayS"] = fsm.Transition("PlayS")
    mainFSM.FSM.transitions["toQuickVolS"] = fsm.Transition("QuickVolS")
    mainFSM.FSM.transitions["toSetVolS"] = fsm.Transition("SetVolS")
    
    #set initial state
    mainFSM.FSM.SetState("InitS")
    
    print("enter main now")
    while inFSM:
        mainFSM.FSM.Go()
        testName = mainFSM.FSM.curStateName
        testTrans = mainFSM.FSM.trans
        
        if testTrans == None: # run and check for transitions
            #print("trans == None")
            #mainFSM.FSM.Go()
            if (testName == "WaitS") | (testName == "InitS"):
                if btns_V1.clickA.implement == False: # set up for each button
                    mainFSM.FSM.Transition("toFilterS")
                    testTrans = mainFSM.FSM.trans
                    btns_V1.clickA.implement = True

                if btns_V1.clickB.implement == False: # set up for each button
                    mainFSM.FSM.Transition("toInstS")
                    testTrans = mainFSM.FSM.trans
                    btns_V1.clickB.implement = True

                if btns_V1.clickC.implement == False: # set up for each button
                    #mainFSM.FSM.Transition("toInitS")
                    #testTrans = mainFSM.FSM.trans
                    print("no use for btn in this state")
                    btns_V1.clickC.implement = True

                if btns_V1.clickD.implement == False: # set up for each button
                    mainFSM.FSM.Transition("toOutputS")
                    testTrans = mainFSM.FSM.trans
                    btns_V1.clickD.implement = True

                if btns_V1.clickE.implement == False: # set up for each button
                    mainFSM.FSM.Transition("toRecordS")
                    testTrans = mainFSM.FSM.trans
                    btns_V1.clickD.implement = True

                if btns_V1.clickF.implement == False: # set up for each button
                    mainFSM.FSM.Transition("toSetVolS")
                    testTrans = mainFSM.FSM.trans
                    btns_V1.clickF.implement = True

                if btns_V1.clickG.implement == False: # set up for each button
                    mainFSM.FSM.Transition("toQuickVolS")
                    testTrans = mainFSM.FSM.trans
                    btns_V1.clickG.implement = True

            if ((testName == "SetVolS") | (testName == "FilterS") | (testName == "InstS") | 
                (testName == "QuickVolS") | (testName == "SetVolS") | (testName == "OutputS")):
                mainFSM.FSM.Transition("toWaitS")
                testTrans = mainFSM.FSM.trans
                
            if (testName == "RecordS"): # stuck on: button doesn't reset to false
                if btns_V1.clickE.implement == False:
                    mainFSM.FSM.Transition("toStoreS")
                    testTrans = mainFSM.FSM.trans
                    btns_V1.clickE.implement = True

            if (testName == "StoreS"):
                if btns_V1.clickC.implement == False:
                    mainFSM.FSM.Transition("toPlayS")
                    testTrans = mainFSM.FSM.trans
                    btns_V1.clickC.implement = True

                if btns_V1.clickD.implement == False:
                    mainFSM.FSM.Transition("toWaitS")
                    testTrans = mainFSM.FSM.trans
                    btns_V1.clickD.implement = True

            if (testName == "PlayS"):
                if btns_V1.clickC.implement == False:
                    mainFSM.FSM.Transition("toPlayS")
                    testTrans = mainFSM.FSM.trans
                    btns_V1.clickC.implement = True

                if btns_V1.clickD.implement == False:
                    mainFSM.FSM.Transition("toWaitS")
                    testTrans = mainFSM.FSM.trans
                    btns_V1.clickD.implement = True

        else: # implement transition and run
            #print("edge case FAIL")
            mainFSM.FSM.Go()
            mainFSM.FSM.Transition(mainFSM.FSM.transName)
            

        
        pass
    
## working fsm but messy, make sure to add Go() after all cases
'''if testName == "InitS": 
            btn1.when_pressed = btns_V1.clickA.clicked
            if btn1.is_pressed:
                btns_V1.clickA.clicked()
                print("state A clicked button")
            if btns_V1.clickA.implement == False:
                print("state A clicked button")
                mainFSM.FSM.Transition("toWaitS")
                btns_V1.clickA.implement = True
            # Testing code: Remove for full implementation
            #lcd.write_lcd("Synth Start    F", "A B C D E      G") # add when import lcd
            #print("Synth Start    F")
            #mainFSM.FSM.Transition("toWaitS")
            #time.sleep(5)
            # End Testing Code

            pass

        elif testName == "WaitS": 
            # button presses will cause transitions to other states
            #btn1.when_pressed = btns_V1.clickA.clicked
            btns_V1.btn2.when_pressed = btns_V1.clickB.clicked()
            btns_V1.btn3.when_pressed = btns_V1.clickC.clicked()
            btns_V1.btn4.when_pressed = btns_V1.clickD.clicked()
            btns_V1.btn5.when_pressed = btns_V1.clickE.clicked()
            btns_V1.btn6.when_pressed = btns_V1.clickF.clicked()
            btns_V1.btn7.when_pressed = btns_V1.clickG.clicked()

            # Testing code: Remove for full implementation
            #mainFSM.FSM.Transition("toInitS")
            #mainFSM.FSM.curStateName = "InitS"
            print("State 2")
            time.sleep(5)
            # End Testing Code

            pass'''
