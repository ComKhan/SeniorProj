# Updates variables and settings upon a button click
# Button Setup:
# Btn6 F - Vol Down     Btn7 G - Vol Up
# Btn1 A    Btn2 B  Btn3 C  Btn4 D  Btn5 E
# FilterMD  Inst            OutMd   Record 
#                   Yes     No       

import array as arr
from fcntl import F_SEAL_SEAL
import string
import RPi.GPIO as GPIO
from gpiozero import Button



# dictionaries to be used as btnClk(clicks) input
recordSet = ["STOP", "START"] # when initialized it begins at STOP, only on next click it STARTS
instSet = ["INSTA", "INSTB", "INSTC"] # cycles through instruments, correspond to library
volSet = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # make separate function that stops at max and min instead of looping around
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



##=======================================================================
# button implementation
#recordBtn = btnClk(recordSet, "Record Button")
clickA = btnClk(filterSet, "A")
clickB = btnClk(instSet, "B")
clickC = btnClk(ynSet, "C")
clickD = btnClk(outputSet, "D")
clickE = btnClk(recordSet, "E")
clickF = btnClk(volSet, "F") #create function for vol down clicked
clickG = btnClk(volSet, "G") 
#global btn1, btn2, btn3, btn4, btn5, btn6, btn7
