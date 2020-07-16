def login(master):
    login_case={
        1: (midX, midY, startX, endX)=face_detection(jaywon)
        2: (midX, midY, startX, endX)=face_detection(afiqah)
        3: (midX, midY, startX, endX)=face_detection(lockhee)
    }
    return login_case.get(master, "not valid")

#master1=face_detection(jaywon)//박스에 붙는 이름 코딩 라벨을 알고 싶음

def detect(name):
    midX=!0 and midX=!0 and startX=!0 and endX=!0 #I DONT KNOW HUHU
    return name

def match():
    if(login(1)==detect(jaywon)):
        jaywon()
    elif(login(2)==detect(afiqah)):
        afiqah()
    elif(login(3)==detect(lockhee)):
        lockhee()
    else:
    return "not valid"

def start():
    #welcome face login gui
    match()
