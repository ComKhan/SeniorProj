# Updates variables and settings upon a button click
# Button Setup:
# Btn6 F - Yes     Btn7 G - No/Output Mode
# Btn1 A    Btn2 B  Btn3 C  Btn4 D  Btn5 E
# VolDwn    VolUp   Record  Filter  Inst 

import array as arr
from fcntl import F_SEAL_SEAL
import string
import RPi.GPIO as GPIO
from gpiozero import Button
import subprocess


# dictionaries to be used as btnClk(clicks) input
recordSet = ["STOP", "START"] # when initialized it begins at STOP, only on next click it STARTS
instSet = ["INSTA", "INSTB", "INSTC"] # cycles through instruments, correspond to library
volSet = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100] # make separate function that stops at max and min instead of looping around
filterSet = ["LIVEMD", "AUTOTUNEMD"]
outputSet = ["SJACK", "LJACK", "MIDI", "NONE"]
ynSet = ["Yes", "No"]


# when a button is clicked you select the corresponding clicks array to cycle through

# don't need this class, use built in Button library functions
class btnClk: # need two -- reset index upon click and store index

    # may need to move this to the init method:
    #settings = setArr # set to the array to cycle through for each object

    def __init__(self, clicks, name): # clicks is the 
        # in/out pin setting
        self.index = 0
        self.clicks = clicks
        self.val = clicks[self.index]
        self.name = name
        self.implement = True # True is default, whenever it's set to False perform the function and reset to True
        pass

    def clicked(self):
        self.implement = False
        if (self.index < len(self.clicks) - 1):
            self.index +=1
        else:
            self.index = 0
        self.val = self.clicks[self.index]
        
        print("Button has been clicked -- " + self.name + str(self.index))
        pass

    def volUpClicked(self):
        self.implement = False
        if (self.index < len(self.clicks) - 1):
            self.index +=1
        else:
            pass #remove if vol control works without this
        self.val = self.clicks[self.index]
        vol = self.val
        cmd = ["amixer", "sset", "Master", "{}%".format(vol)]
        subprocess.Popen(cmd)

    def volDwnClicked(self):
        self.implement = False
        if (self.index >= 1):
            self.index -=1
        else:
            pass #remove if vol control works without this
        self.val = self.clicks[self.index]
        vol = self.val
        cmd = ["amixer", "sset", "Master", "{}%".format(vol)]
        subprocess.Popen(cmd)
        

##=======================================================================
# button implementation
#recordBtn = btnClk(recordSet, "Record Button")
clickA = btnClk(volSet, "A")
clickB = btnClk(volSet, "B")
clickC = btnClk(recordSet, "C")
clickD = btnClk(filterSet, "D")
clickE = btnClk(instSet, "E")
clickF = btnClk(ynSet, "F") #create function for vol down clicked
clickG = btnClk(ynSet, "G")

clickVol = btnClk(volSet, "Vol")
#global btn1, btn2, btn3, btn4, btn5, btn6, btn7
