from omniwheel.motor import *
from omniwheel.ultrasonic import *
from recognize_video_func import *

def start_search_master():
    rotateLeft()
    time.sleep(1.0)
    stop()
    time.sleep(5.0)

def master_found():
    (midX, midY, startX, startY)=face_detection(master)
    
def master_not_found():
    (midX, midY, startX, endX)=face_detection(master)
    midX==0 and midY==0 and startX==0 and startY==0
    
def go_master():
    cbox= (startX+endX)/2
    
    if(h <=cbox <= w):
        for i in range(20):
            forward()
            distance= get_distance()
            time.sleep(0.05)

            if distance >= 30:
                green_light()
                
            elif distance <= 10:
                red_light()
                stop()
                #GUI SUCCESS! +LED?
        
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