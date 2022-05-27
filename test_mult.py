import multiprocessing
import btns
import rootFSM as fsm


import signal
import sys
import RPi.GPIO as GPIO

BUTTON_GPIO = 5


def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)

def button_pressed_callback(channel):
    print("Button pressed!")
    btns.clickC.clicked()
    button_press.value = 1
    #button_press3.value = 1
    
def process_1(button_press):
    i = 0
    print("running")
    '''fsm.btn5.when_pressed = btns.clickE.clicked
    if (btns.clickE.implement == False):
        button_press1.value = 1
        print("p1 click")
        btns.clickE.implement = True


    while button_press.value != 1:
        fsm.btn5.when_pressed = btns.clickE.clicked
        if (btns.clickE.implement == False):
            button_press1.value = 1
            print("p1 click")
            btns.clickE.implement = True'''

    while button_press.value != 1:
        if (i%200000 == 0):
            print(i)
            pass
        i = i+1

    '''fsm.btn5.when_pressed = btns.clickE.clicked
    if (btns.clickE.implement == False):
        button_press1.value = 1
        print("p1 click")
        btns.clickE.implement = True'''


    print("done")


def process_2(button_press):
    #print("p2 go")
    #fsm.btn5.when_pressed = btns.clickE.clicked
    if (btns.clickC.implement == False):
        button_press.value = 1
        print("p1 click")
        btns.clickC.implement = True

    while button_press.value != 1:
        #print("yes")
        #fsm.btn3.when_pressed = btns.clickC.clicked
        if (btns.clickC.implement == False):
            button_press.value = 1
            print("p2 click")
            #btns.clickC.
            btns.clickC.implement = True

        #i = i+1

    if button_press.value == 1:
        print('button works')
    
    
    print("done2")

button_press = multiprocessing.Value('i')
button_press.value = 0

if __name__ == "__main__":
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(BUTTON_GPIO, GPIO.FALLING, 
        callback=button_pressed_callback, bouncetime=300)
    #signal.signal(signal.SIGINT, signal_handler)
    #signal.pause()

    

    p = multiprocessing.Process(target = (process_1), args=(button_press,))
    p1 = multiprocessing.Process(target = (process_2), args = (button_press,))


    p.start()
    p1.start()
    p.join()
    p1.join()
