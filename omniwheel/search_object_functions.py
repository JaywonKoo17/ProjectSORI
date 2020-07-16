from omniwheel.motor import *
#from recognize_video_func import * //for object
from omniwheel.ultrasonic import *

setupult()
setup()


h = 260
w = 300
midsr=50


def start_search_object():
    rotateLeft()
    time.sleep(1.0)
    stop()
    time.sleep(5.0)

def object_found_1(): 
    (midX, midY, startX, endX)=object_detection(bottle)
    
def object_found_2():
    (midX, midY, startX, startY)=object_detection(?)
    
def object_found_3():
    (midX, midY, startX, startY)=object_detection(?)
    
def start_moving():
    green_light()
    cbox= (startX+endX)/2
    if(h <= cbox <= w):
        for i in range(20):
            forward()
            distance= get_distance()
            time.sleep(0.05)
                
            if distance <= 20:
                red_light()
                stop()

    elif(cbox <= h):
        for i in range(20):
            rotateLeft()
            
    elif(cbox >= w):
        for i in range(20):
            rotateRight()
            
    else:
        
        if key == ord("q"):
            stop()
            break

def not_found():
    (midX, midY, startX, endX)=object_detection(bottle)
    midX==0 and midY==0 and startX==0 and startY==0
    #i dont know huhu
