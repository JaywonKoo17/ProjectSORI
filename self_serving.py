#self_serving mode: choose object -> find object -> find person
from object_detect_all import *

#GUI "what do you need?" -> assign f_obj
#end GUI
def self_serving(ID):
    result = object_detect_func(f_obj) #0: found  1: failed

    #object detected-> find person
    if(result == 1):
        #GUI : "GO!"
        #end GUI
        face_detect_func(ID)
            # if detected GUI sucess 
        


