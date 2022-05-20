import multiprocessing
import btns
import rootFSM as fsm

def process_1(button_press1):
    i = 0

    while button_press.value != 1:
        fsm.btn5.when_pressed = btns.clickE.clicked
        if (btns.clickE.implement == False):
            button_press1.value = 1
            print("p1 click")

        print(i)
        i = i+1



def process_2(button_press2):

    i = 0
    while button_press.value == 0:
        fsm.btn5.when_pressed = btns.clickE.clicked
        if (btns.clickE.implement == False):
            button_press2.value = 1
            print("p1 click")
            btns.clickE.c
        i = i+1

    if button_press.value == 1:
        print('button works')



if __name__ == "main":

    button_press = multiprocessing.Value('i')
    button_press.value = 0
    p = multiprocessing.Process(target = (process_1), args=(button_press))
    p1 = multiprocessing.Process(target = (process_2), args = (button_press))


    p.start()
    p1.start()
    p.join()
    p1.join()
