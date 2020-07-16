import time
from omniwheel.search_object_functions import *

round=0

def search_object_1():
    if object_found_1():
        for start_moving():
            #gui GO
            green_light()#need or not

    elif not_found():
        for round=<5:
            start_search_object()
            
        else:
            stop()
            #gui "can't find object 1"
        
    else:
            #exitbutton() and stop()

def search_object_2():
                
    if object_found_2():
        for start_moving():
            #gui GO
            led_green()

    elif not_found():
        for round=<5:
            start_search_object()
            
        else:
            stop()
            #gui "can't find object 1"
        
    else:
            #exitbutton() and stop()

def search_object_3():        
    if object_found_3():
        for start_moving():
            #gui GO
            green_light()
        
    elif not_found():
        for round=<5:
            start_search_object()
            
        else:
            stop()
            #gui "can't find object 1"
        
    else:
            #exitbutton() and stop()