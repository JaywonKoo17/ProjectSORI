from omniwheel.motor import *
from omniwheel.ultrasonic import *
from omniwheel.search_person_functions import *
from object_detect import *

#found  = find_obj("banana")
#if found ==1 :
#    print("success")
#else:
#    print("wrong")


def object_detect_func(f_obj):
    setupult()
    setup()


    #h = 260   
    #w = 300
    #midsr=50
    r = 0
    end = 0 # 0: fail 1:found 

    #GUI get input
    #f_obj = "laptop"

    while(True):
        detect = find_obj(f_obj)
        
        #detected wrong
        if( detect == 0):
            if r<5:
                print("cannot find object!!")
                start_search_person()
                r=r+1
            else: #still not found -> goto fail GUI
                end = 0
                break
            
        #found right person
        elif(detect == 1):              
            for i in range(100):
                forward()
                print ("forward")
                distance= get_distance()
                time.sleep(0.05)
                print(distance)
                    
                #arrived to person 
                if distance <= 20:
                    stop()
                    print ("arrived and stop")
                    end = 1
                    break
        else:
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                stop()
                print("quit")
                break
            
        #if arrived at the person, end this function
        if end == 1 :
            break
        
    return end
  

object_detect_func()
print("finish")
