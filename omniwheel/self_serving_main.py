import time

round=0

def self_serving():
    #gui "what do you need"?
    if(object_1):#object_1 button pushed
        object_found_1()
        for start_moving():
                #gui GO
                led_green()
                
    elif(object_2):#object_2 button pushed
        object_found_2()
        for start_moving():
            #gui GO
            led_green()
            
    elif (object_3):#object_3 button pushed
        object_found_3()
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
            #exitbutton()