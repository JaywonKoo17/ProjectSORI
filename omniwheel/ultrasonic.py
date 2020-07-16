import RPi.GPIO as GPIO
import time


TRIG = 33
ECHO = 35
GREEN = 37
RED = 32
    
def setupult():
    GPIO.setwarnings(False)
    GPIO.cleanup() 
    GPIO.setmode(GPIO.BOARD) #follow the gpio not the pin number

    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)
    GPIO.setup(GREEN,GPIO.OUT)
    GPIO.setup(RED,GPIO.OUT)

def green_light_on():
    GPIO.output(GREEN, GPIO.HIGH)
    GPIO.output(RED, GPIO.LOW)
    
def green_light_off():
    GPIO.output(GREEN, GPIO.LOW)
    GPIO.output(RED, GPIO.LOW)

def red_light():
    GPIO.output(GREEN, GPIO.LOW)
    GPIO.output(RED, GPIO.HIGH)

def get_distance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == False:
        start = time.time()
    while GPIO.input(ECHO) == True:
        end = time.time()

    signal_time = end-start
    distance = signal_time / 0.000058

    return distance
