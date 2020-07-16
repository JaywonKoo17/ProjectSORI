from face_detect_func import *
from omniwheel.motor import *
from self_serving import *
from delivery import *

setuplt()
setup()

while(True):
    #GUI "start"
    ID = face_login()
    print(ID)
    
    if(ID == "none"):
        #GUI "who are u?"
        print("who are u")
    else:
        #select Mode GUI
        #if selfserving
        self_serving(ID)
        
        #if delivery
        delivery(ID)
    

