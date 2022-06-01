#imports for file storage
import threading

# https://www.youtube.com/watch?v=E45v2dD3IQU&ab_channel=TrevorPayne
from operator import truediv
from tkinter import NONE
from types import prepare_class
from random import randint
import time
import btns

# imports for buttons.py
import RPi.GPIO as GPIO
from gpiozero import Button
import main
import lcd
import subprocess
import noteMatch
import wavFuncs
import noteMatch
State = type("States", (object,), {})
btn1 = Button(16) #Filter, Yes
btn2 = Button(6) # Inst
btn3 = Button(5) # No
btn4 = Button(0) # Output
btn5 = Button(4) # Record
#btn6 = Button(3) # Vol Dwn
#btn7 = Button(2) # Vol Up

class InitS(State):
    def __init__(self):
        
        print("Init InitS")
        pass

    def Go(self):
        #btns.initialize()
        #print("go InitS")
        #time.sleep(2)
        btn1.when_pressed = btns.clickVol.volDwnClicked
        btn2.when_pressed = btns.clickVol.volUpClicked
        btn3.when_pressed = btns.clickC.clicked
        btn4.when_pressed = btns.clickD.clicked
        btn5.when_pressed = btns.clickE.clicked
        #btn6.when_pressed = btns.clickF.clicked
        #btn7.when_pressed = btns.clickG.clicked
        
        #lcd.write_lcd("Click any button\n","to start")
        '''if btn1.is_pressed: # wait  for button clicks within states
            btns.clickA.clicked()
            print("state A clicked button")'''
        '''if btns.clickA.implement == False: # check for button click updates in main, bc transitions should be triggered there
            print("state A clicked button")
            mainFSM.FSM.Transition("toWaitS")
            btns.clickA.implement = True'''
        pass
    

class WaitS(State):
    def __init__(self):
        # update variable corresponding to the button
        
        pass

    def Go(self):
        #print("go WaitS")
        #lcd.write_lcd("Settings     Yes\n","A  B  C  D  E  No")
        btn1.when_pressed = btns.clickVol.volDwnClicked
        btn2.when_pressed = btns.clickVol.volUpClicked
        btn3.when_pressed = btns.clickC.clicked
        
        btn4.when_pressed = btns.clickD.clicked
        btn5.when_pressed = btns.clickE.clicked
        #btn6.when_pressed = btns.clickF.clicked
        #btn7.when_pressed = btns.clickG.clicked # no function to increment in wait, implement flag may get messed up for btn if left in
        # Testing code: Remove for full implementation
        #mainFSM.FSM.Transition("toInitS")
        #mainFSM.FSM.curStateName = "InitS"
        
        pass


class RecordS(State):
    def __init__(self):
        # update variable corresponding to the button
        
        pass

    def Go(self):
        btn1.when_pressed = btns.clickVol.volDwnClicked
        btn2.when_pressed = btns.clickVol.volUpClicked
        btn3.when_pressed = btns.clickC.clicked
        #lcd.write_lcd("Recording\n","Volume ") # add volume variable
        
        stop_flag = fin_flag = 0
        thread = threading.Thread(target=noteMatch.dynamicRecording)
        thread.start()
        btns.clickC.implement = True
        lcd.write_lcd("recording", "")
        while fin_flag != 1:
            if btns.clickC.implement == False:
                noteMatch.stop_flag = 1
                fin_flag = 1
                lcd.write_lcd("stopping\n","")
        lcd.write_lcd("recording\n","done")
        thread.join()
        noteMatch.playback(btns.clickE.val, btns.clickD.val)
        #noteMatch.autoTune(btns.clickE.val, btns.clickD.val)
        
        #btns.clickC.implement = True
        pass

class StoreS(State):
    def __init__(self):
        # update variable corresponding to the button
        
        pass

    def Go(self):
        # Perform storing functions first / use flag to only do once
        #lcd.write_lcd("Play file?   Yes\n","            No")
        #btn6.when_pressed = btns.clickF.clicked
        #btn7.when_pressed = btns.clickG.clicked
        pass

class PlayS(State):
    def __init__(self):
        # update variable corresponding to the button
        
        pass

    def Go(self):
        #lcd.write_lcd("Playing file")
        btn1.when_pressed = btns.clickVol.volDwnClicked
        btn2.when_pressed = btns.clickVol.volUpClicked

        pass

class QuickVolS(State):
    def __init__(self):
        # update variable corresponding to the button
        print("Init QuickVolS")
        pass

    def Go(self):
        btn1.when_pressed = btns.clickVol.volDwnClicked
        btn2.when_pressed = btns.clickVol.volUpClicked
        
        print("go QuickVolS")

        '''if (btns.clickVol.implement == False): # works from btns for now, wasn't working in fsm
            vol = btns.clickVol.val
            cmd = ["amixer", "sset", "Master", "{}%".format(vol)]
            subprocess.Popen(cmd)
            btns.clickVol.implement = True'''
        pass

class SetVolS(State):
    def __init__(self):
        # update variable corresponding to the button
        print("Init SetVolS")
        pass

    def Go(self):
        print("go SetVolS")
        btn1.when_pressed = btns.clickVol.volDwnClicked
        btn2.when_pressed = btns.clickVol.volUpClicked

        '''if (btns.clickVol.implement == False): # works from btns for now, wasn't working in fsm
            vol = btns.clickVol.val
            cmd = ["amixer", "sset", "Master", "{}%".format(vol)]
            subprocess.Popen(cmd)
            btns.clickVol.implement = True'''
        pass
        pass

class InstS(State):
    def __init__(self):
        # update variable corresponding to the button
        print("Init SetInstS")
        pass

    def Go(self):
        print("go SetInstS")
        pass

class FilterS(State):
    def __init__(self):
        # update variable corresponding to the button
        print("Init SetFilterS")
        pass

    def Go(self):
        print("go SetFilterS")
        pass

class OutputS(State):
    def __init__(self):
        # update variable corresponding to the button
        print("Init SetOutS")
        pass

    def Go(self):
        print("go SetOutS")
        pass


##============================================================================

class Transition():
    def __init__(self, toState):
        self.toState = toState
        #self.curState = toState
        #self.curStateName = toState
        print("trans init")

    def Go(self):
        #self.toState = toState
        #self.SetState(self.toState)
        #self.curStateName = self.toState
        print("trans go")

##============================================================================

class SimpleFSM(object):
    def __init__(self, char):
        self.char = char
        self.states = {}        # state dictionary
        self.transitions = {}   # transition dictionary
        self.curState = None    # current state
        self.curStateName = None
        self.trans = None       # current transition
        self.transName = None
        self.lcd = True
        self.lcdShort = True # short 2 sec flag for settings messages
        print("Init simpFSM")

    def SetState(self, stateName): # look at string passed within dictionary
        self.curState = self.states[stateName]  # paired with a state instance
        self.curStateName = stateName
        print("set state simpFSM")

    def Transition(self, transName):  
        self.trans = self.transitions[transName]
        self.transName = transName
        self.lcd = False
        print("trans simpFSM")

    def Go(self):
        if(self.trans):             # if there's a transition stored within the trans
            self.trans.Go()    # execute that transition
            self.SetState(self.trans.toState) # set to transitioned state
            self.transName = None
            self.lcd = True
            self.lcdShort = True
            print("in state " + self.curStateName)
            self.trans = None       # reset transition to None
        self.curState.Go()     # execute current state
        #print("go simpfsm")

##============================================================================ 
# holds all character attributes and properties
# FSM is stored within this class

class Char(object):
    def __init__(self):
        self.FSM = SimpleFSM(self) # create an instance of the fsm
        self.Set = True # store propery to true
        print("char init")


##============================================================================