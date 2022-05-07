# https://www.youtube.com/watch?v=E45v2dD3IQU&ab_channel=TrevorPayne
from operator import truediv
from tkinter import NONE
from types import prepare_class
from random import randint
import time
import btns

#import lcd

State = type("States", (object,), {})


class InitS(State):
    def __init__(self):
        
        print("Init InitS")
        pass

    def Go(self):
        btns.initialize()
        print("go InitS")
    

class WaitS(State):
    def __init__(self):
        # update variable corresponding to the button
        print("Init WaitS")
        pass

    def Go(self):
        print("go WaitS")
        pass


class RecordS(State):
    def __init__(self):
        # update variable corresponding to the button
        print("Init RecordS")
        pass

    def Go(self):
        print("go RecordS")
        pass

class StoreS(State):
    def __init__(self):
        # update variable corresponding to the button
        print("Init StoreS")
        pass

    def Go(self):
        print("go StoreS")
        pass

class PlayS(State):
    def __init__(self):
        # update variable corresponding to the button
        print("Init PlayS")
        pass

    def Go(self):
        print("go PlayS")
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

class SetInstS(State):
    def __init__(self):
        # update variable corresponding to the button
        print("Init SetInstS")
        pass

    def Go(self):
        print("go SetInstS")
        pass

class SetFilterS(State):
    def __init__(self):
        # update variable corresponding to the button
        print("Init SetFilterS")
        pass

    def Go(self):
        print("go SetFilterS")
        pass

class SetOutS(State):
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
        #self.curState = toState
        #self.curStateName = toState
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
        print("Init simpFSM")

    def SetState(self, stateName): # look at string passed within dictionary
        self.curState = self.states[stateName]  # paired with a state instance
        self.curStateName = stateName
        print("set state simpFSM")

    def Transition(self, transName):  
        self.trans = self.transitions[transName]
        print("trans simpFSM")

    def Go(self):
        if(self.trans):             # if there's a transition stored within the trans
            self.trans.Go()    # execute that transition
            self.SetState(self.trans.toState) # set to transitioned state
            self.trans = None       # reset transition to None
        self.curState.Go()     # execute current state
        print("go simpfsm")

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
inFSM = True # stays in FSM while true

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
        match mainFSM.FSM.curStateName:
            case "InitS":
                #lcd.write_lcd("Synth Start    F", "A B C D E      G") # add when import lcd
                print("Synth Start    F")
                mainFSM.FSM.Transition("toWaitS")
                time.sleep(5)
                pass

            case "WaitS":
                mainFSM.FSM.Transition("toInitS")
                mainFSM.FSM.curStateName = "InitS"
                print("State 2")
                time.sleep(5)
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
    '''
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
