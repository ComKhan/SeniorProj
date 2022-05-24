import multiprocessing
import btns
import rootFSM as fsm

def process_1(button_press1):
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

    while  button_press1 != 1:
        if (i%2000 == 0):
            #print(i)
            pass
        i = i+1

    '''fsm.btn5.when_pressed = btns.clickE.clicked
    if (btns.clickE.implement == False):
        button_press1.value = 1
        print("p1 click")
        btns.clickE.implement = True'''


    print("done")


def process_2(button_press2):
    #print("p2 go")
    fsm.btn5.when_pressed = btns.clickE.clicked
    if (btns.clickE.implement == False):
        button_press2.value = 1
        print("p1 click")
        btns.clickE.implement = True

    while button_press.value != 1:
        #print("yes")
        fsm.btn5.when_pressed = btns.clickE.clicked
        if (btns.clickE.implement == False):
            button_press2.value = 1
            print("p2 click")
            btns.clickE.c
            btns.clickE.implement = True

        #i = i+1

    if button_press.value == 1:
        print('button works')

    print("done2")



if __name__ == "__main__":

    button_press = multiprocessing.Value('i')
    button_press.value = 0

    p = multiprocessing.Process(target = (process_1), args=(button_press,))
    p1 = multiprocessing.Process(target = (process_2), args = (button_press,))


    p.start()
    p1.start()
    p.join()
    p1.join()
