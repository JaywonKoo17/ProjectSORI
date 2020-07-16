def search_master():
    if master_found():
        go_master()
        
    elif master_not_found():
        for round=<5:
            start_search_master()
            #gui "GO!"
        else:
            stop()
            #gui "master_not_found"
    else:
        #gui exitbutton() pushed and stop()