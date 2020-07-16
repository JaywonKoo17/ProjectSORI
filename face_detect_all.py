from face_detect_func import *
from omniwheel.motor import *
from omniwheel.ultrasonic import *
from omniwheel.search_person_functions import *

"""
ID = face_login()

result = face_detect_name(ID)
if(result == 1):
    print("success")
else:
    print("fail")

"""
def face_detect_func(f_per):
    setupult()
    setup()


    #h = 200
    #w = 360
    #midsr=50
    r = 0
    end = 0 # 0: fail 1:found


    #ID = face_login()  #login function
    #print(ID)


    while(True):
        detect = face_detect_name(f_per)
        
        #detected wrong
        if( detect == 0):
            if r<5:
                print("cannot find person!!")
                start_search_person()
                r=r+1
            else: #still not found -> goto fail GUI
                end = 0
                red_light()
                break
        #found right person
        elif(detect == 1):              
            for i in range(100):
                forward()
                green_light_on()
                time.sleep(0.3)
                green_light_off()
                time.sleep(0.3)
                print ("forward")
                distance= get_distance()
                time.sleep(0.05)
                print(distance)
                    
                #arrived to person 
                if distance <= 20:
                    stop()
                    print ("arrived and stop")
                    for c in range(3):
                        green_light_on()
                        time.sleep(0.3)
                        green_light_off()
                        time.sleep(0.3)
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
  

result = face_detect_func("Jaywon")

if(result == 1):
    print("success")
else:
    print("Fail")


