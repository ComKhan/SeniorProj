# https://www.youtube.com/watch?v=E45v2dD3IQU&ab_channel=TrevorPayne
from operator import truediv
from tkinter import NONE
from types import prepare_class
from random import randint
import time
import btns_V1
# imports for buttons.py
import RPi.GPIO as GPIO
from gpiozero import Button
#import demo_v1_wk7.main as main
#import main
#import lcd_V1

#import auRec as au

State = type("States", (object,), {})
btn1 = Button(16) #Filter, Yes
btn2 = Button(6) # Inst
btn3 = Button(5) # No
btn4 = Button(0) # Output
btn5 = Button(4) # Record
btn6 = Button(3) # Vol Dwn
btn7 = Button(2) # Vol Up

# Initi LCD
from subprocess import Popen, PIPE
from time import sleep
from datetime import datetime
import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd

# Modify this if you have a different sized character LCD
lcd_columns = 16
lcd_rows = 2

# compatible with all versions of RPI as of Jan. 2019
# v1 - v3B+
lcd_rs = digitalio.DigitalInOut(board.D27)
lcd_en = digitalio.DigitalInOut(board.D17)
lcd_d4 = digitalio.DigitalInOut(board.D22)
lcd_d5 = digitalio.DigitalInOut(board.D23)
lcd_d6 = digitalio.DigitalInOut(board.D24)
lcd_d7 = digitalio.DigitalInOut(board.D25)


# Initialise the lcd class
lcd = characterlcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6,
                                      lcd_d7, lcd_columns, lcd_rows)

# run unix shell command, return as ASCII
def run_cmd(cmd):
    p = Popen(cmd, shell=True, stdout=PIPE)
    output = p.communicate()[0]
    return output.decode('ascii')

def write_lcd(line1, line2):
    lcd.clear()
    lcd_line_1 = str(line1)
    lcd_line_2 = str(line2)
    lcd.message = lcd_line_1 + lcd_line_2

'''#Alberto's code
import multiprocessing
import pyaudio
import numpy as np
from scipy.fft import fft,ifft
from scipy.signal import hilbert
import wave
import np2
import time
from fir_filter import fir_filt
import wave

form_1 = pyaudio.paInt16
chans = 1
samp_rate = 48000
chunk =4096
record_secs = 5
dev_index = 1   #this is the device index (usb device specific port) connection in hardware VARIES
#wav_output_filename = 'test6.wav'
audio = pyaudio.PyAudio()

stream = audio.open(format = form_1, rate = samp_rate, channels = chans, \
                    input_device_index = dev_index, input = True, \
                    frames_per_buffer = chunk)
data= multiprocessing.Value('i')
data.value= 0

queue_count = multiprocessing.Value('i')
queue_count.value = 0

final_freq = multiprocessing.Array('f',4096)

final_vol= multiprocessing.Array('i',4096)'''


class InitS(State):
    def __init__(self):
        
        print("Init InitS")
        pass

    def Go(self):
        #btns_V1.initialize()
        print("go InitS")
        time.sleep(2)
        btn1.when_pressed = btns_V1.clickA.clicked
        btn2.when_pressed = btns_V1.clickB.clicked
        btn3.when_pressed = btns_V1.clickC.clicked
        btn4.when_pressed = btns_V1.clickD.clicked
        btn5.when_pressed = btns_V1.clickE.clicked
        btn6.when_pressed = btns_V1.clickF.clicked
        btn7.when_pressed = btns_V1.clickG.clicked
        lcd_line_1 = "Initializing... "
        lcd_line_2 = "Init test"
        lcd.message = lcd_line_1 + lcd_line_2
        '''if btn1.is_pressed: # wait  for button clicks within states
            btns_V1.clickA.clicked()
            print("state A clicked button")'''
        '''if btns_V1.clickA.implement == False: # check for button click updates in main, bc transitions should be triggered there
            print("state A clicked button")
            mainFSM.FSM.Transition("toWaitS")
            btns_V1.clickA.implement = True'''
        pass
    

class WaitS(State):
    def __init__(self):
        # update variable corresponding to the button
        
        pass

    def Go(self):
        #print("go WaitS")
        btn1.when_pressed = btns_V1.clickA.clicked
        btn2.when_pressed = btns_V1.clickB.clicked
        btn3.when_pressed = btns_V1.clickC.clicked
        btn4.when_pressed = btns_V1.clickD.clicked
        btn5.when_pressed = btns_V1.clickE.clicked
        btn6.when_pressed = btns_V1.clickF.clicked
        btn7.when_pressed = btns_V1.clickG.clicked
        lcd_line_1 = "Waiting for "
        lcd_line_2 = "btn"
        lcd.message = lcd_line_1 + lcd_line_2
        # Testing code: Remove for full implementation
        #mainFSM.FSM.Transition("toInitS")
        #mainFSM.FSM.curStateName = "InitS"
        
        pass


class RecordS(State):
    def __init__(self):
        # update variable corresponding to the button
        
        pass

    def Go(self):
        btn5.when_pressed = btns_V1.clickE.clicked
        
        pass

class StoreS(State):
    def __init__(self):
        # update variable corresponding to the button
        
        pass

    def Go(self):
        btn3.when_pressed = btns_V1.clickC.clicked
        btn4.when_pressed = btns_V1.clickD.clicked
        '''q = multiprocessing.Queue()
        p = multiprocessing.Process(target = au.get_data,args = (stream,samp_rate,chunk,q,data,audio))
        p1 = multiprocessing.Process(target = au.get_freq, args = (samp_rate,chunk,q,data,final_freq,final_vol,queue_count))
    
        tic = time.time()
        p.start()
        p1.start()
        p.join()
        p1.join()
        
        toc = time.time()
        print(list(final_freq[:]))
        print(queue_count.value)
        print(toc-tic)
        i = 0'''
        pass

class PlayS(State):
    def __init__(self):
        # update variable corresponding to the button
        
        pass

    def Go(self):
        btn3.when_pressed = btns_V1.clickC.clicked
        btn4.when_pressed = btns_V1.clickD.clicked
        pass

class QuickVolS(State):
    def __init__(self):
        # update variable corresponding to the button
        print("Init QuickVolS")
        pass

    def Go(self):
        print("go QuickVolS")
        pass

class SetVolS(State):
    def __init__(self):
        # update variable corresponding to the button
        print("Init SetVolS")
        pass

    def Go(self):
        print("go SetVolS")
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
        print("Init simpFSM")

    def SetState(self, stateName): # look at string passed within dictionary
        self.curState = self.states[stateName]  # paired with a state instance
        self.curStateName = stateName
        print("set state simpFSM")

    def Transition(self, transName):  
        self.trans = self.transitions[transName]
        self.transName = transName
        print("trans simpFSM")

    def Go(self):
        if(self.trans):             # if there's a transition stored within the trans
            self.trans.Go()    # execute that transition
            self.SetState(self.trans.toState) # set to transitioned state
            self.trans = None       # reset transition to None
            self.transName = None
            print("in state " + self.curStateName)
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
'''
if __name__ == "__main__":
    light = SimpleFSM()

    light.states["Set"] = Set() #instance of Set state stored within state dictionary inside FSM
    light.states["Off"] = Clicked()
    light.transitions["toOn"] = Transition("Set") # create instance of those transitions and store them within trans dictionary
    light.transitions["toOff"] = Transition("Off")

    #set initial state
    light.SetState("Set")

    for i in range(20):
        timeInterval = 1
        
        if (randint(0,2)):
            if(light.Set):
                light.Transition("toOff")
                #light.Set = False
            else:
                light.Transition("toOn")
                #light.Set = True

        light.Go()


'''
# method in video, using Char method
'''inFSM = True # stays in FSM while true

if __name__ == "__main__":
    mainFSM = Char() # create an instance of the FSM
    
    # add states instances
    mainFSM.FSM.states["InitS"] = InitS() #instance of Set state stored within state dictionary inside FSM
    mainFSM.FSM.states["WaitS"] = WaitS()
    mainFSM.FSM.transitions["toWaitS"] = Transition("WaitS") # create instance of those transitions and store them within trans dictionary
    mainFSM.FSM.transitions["toInitS"] = Transition("InitS")
    
    #set initial state
    mainFSM.FSM.SetState("InitS")

    print("enter main now")
    while inFSM:
        matchName = mainFSM.FSM.curStateName
        if matchName == "InitS":
            #lcd.write_lcd("Synth Start    F", "A B C D E      G") # add when import lcd
            print("Synth Start    F")
            mainFSM.FSM.Transition("toWaitS")
            time.sleep(5)
            pass

        elif matchName == "WaitS":
            mainFSM.FSM.Transition("toInitS")
            mainFSM.FSM.curStateName = "InitS"
            print("State 2")
            time.sleep(5)
            pass

        elif matchName == "RecordS":

            pass

        elif matchName == "StoreS":

            pass
        
        elif matchName == "PlayS":

            pass

        elif matchName == "QuickVol":

            pass

        elif matchName == "SetVolS":

            pass
            
        elif matchName == "SetInstS":

            pass

        elif matchName == "SetFilterS":

            pass

        elif matchName == "SetOutS":

            pass   

        else:
            print("edge case: FAIL")
            pass

        mainFSM.FSM.Go()
        pass
    
    for i in range(20):
        timeInterval = 1
        
        if (randint(0,2)):
            if(light.Set):
                light.FSM.Transition("toOff")
                light.Set = False
            else:
                light.FSM.Transition("toOn")
                light.Set = True

        light.FSM.Go()

    '''
