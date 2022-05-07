# Updates variables and settings upon a button click
# Button Setup:
# Btn1      Btn2    Btn3    Btn4    Btn5
# FilterMD  Inst            OutMd   Record 
# Yes       No

import array as arr
import RPi.GPIO as GPIO
from gpiozero import Button



# dictionaries to be used as btnClk(clicks) input
recordSet = arr(i, ["STOP", "START"]) # when initialized it begins at STOP, only on next click it STARTS
instSet = arr(i, ["INSTA", "INSTB", "INSTC"]) # cycles through instruments, correspond to library
volSet = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # make separate function that stops at max and min instead of looping around
filterSet = ["LIVEMD", "AUTOTUNEMD"]
outputSet = ["SJACK", "LJACK", "MIDI", "NONE"]


def initialize():
    # Button init variables
    global btn1, btn2, btn3, btn4, btn5, btn6, btn7
    btn1 = Button(16)
    btn2 = Button(6)
    btn3 = Button(5)
    btn4 = Button(0)
    btn5 = Button(4)
    btn6 = Button(3)
    btn7 = Button(2)



# when a button is clicked you select the corresponding clicks array to cycle through

# don't need this class, use built in Button library functions
class btnClk(setArr, name): # need two -- reset index upon click and store index

    # may need to move this to the init method:
    settings = setArr # set to the array to cycle through for each object

    def __init__(self, clicks, name): # clicks is the 
        # in/out pin setting
        self.index = 0
        self.val = clicks[self.index]
        self.name = name
        pass

    def clicked(self):
        if (self.index < self.clicks.len() - 1):
            self.index +=1
        else:
            self.index = 0
        self.val = self.clicks[self.index]
        mainFSM.FSM.Transition("toWaitS")
        print("Button has been clicked -- " + self.name + self.index)
        pass





##=======================================================================
# button implementation
recordBtn = btnClk(recordSet, "Record Button")

'''
print("GPIO SETUP")
# GPIO SETUP
GPIO.setwarnings(False) # check function
GPIO.setmode(GPIO.BCM)
GPIO.setup(36, GPIO.IN) # BTN1a
GPIO.setup(31, GPIO.IN) # BTN2
GPIO.setup(29, GPIO.IN) # BTN3
GPIO.setup(27, GPIO.IN) # BTN4
GPIO.setup(7, GPIO.IN) # BTN5
GPIO.setup(5, GPIO.IN) # BTN6
GPIO.setup(3, GPIO.IN) # BTN7
'''
print("gpiozero button functions")
def btnTest():
    print("BTN clicked!")
btn1 = Button(16)
btn2 = Button(6)
btn3 = Button(5)
btn4 = Button(0)
btn5 = Button(4)
btn6 = Button(3)
btn7 = Button(2)
btn1.when_pressed = btnTest
btn2.when_pressed = btnTest
btn3.when_pressed = btnTest
btn4.when_pressed = btnTest
btn5.when_pressed = btnTest
btn6.when_pressed = btnTest
btn7.when_pressed = btnTest