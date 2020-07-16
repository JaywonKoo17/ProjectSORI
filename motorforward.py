import time

import RPi.GPIO as GPIO

 
def setup():
    GPIO.setmode(GPIO.BOARD)

    GPIO.setwarnings(False);

     

    GPIO.setup(22, GPIO.OUT) # Connected to STBY

    # Motor driver 1

    GPIO.setup(12, GPIO.OUT) # Connected to PWMA

    GPIO.setup(3, GPIO.OUT) # Connected to AIN2

    GPIO.setup(5, GPIO.OUT) # Connected to AIN1

    GPIO.setup(7, GPIO.OUT) # Connected to BIN1

    GPIO.setup(11, GPIO.OUT) # Connected to BIN2

    GPIO.setup(13, GPIO.OUT) # Connected to PWMB

    # Motor driver 2

    GPIO.setup(18, GPIO.OUT) # Connected to PWMA

    GPIO.setup(29, GPIO.OUT) # Connected to AIN2

    GPIO.setup(31, GPIO.OUT) # Connected to AIN1

    GPIO.setup(36, GPIO.OUT) # Connected to BIN1

    GPIO.setup(38, GPIO.OUT) # Connected to BIN2

    GPIO.setup(19, GPIO.OUT) # Connected to PWMB

 
# Drive the motor forward
def forward():
    # Motor A:

    GPIO.output(3, GPIO.LOW) # Set AIN1

    GPIO.output(5, GPIO.HIGH) # Set AIN2

    # Motor B:

    GPIO.output(7, GPIO.LOW) # Set BIN1

    GPIO.output(11, GPIO.HIGH) # Set BIN2

    # Motor C:

    GPIO.output(29, GPIO.LOW) # Set AIN1

    GPIO.output(31, GPIO.HIGH) # Set AIN2

    # Motor D:

    GPIO.output(36, GPIO.LOW) # Set AIN1

    GPIO.output(38, GPIO.HIGH) # Set AIN2

    # Set the motor speed

    GPIO.output(12, GPIO.HIGH) # Set PWMA
    
    GPIO.output(13, GPIO.HIGH) # Set PWMB
    
    GPIO.output(18, GPIO.HIGH) # Set PWMA
    
    GPIO.output(19, GPIO.HIGH) # Set PWMB

    GPIO.output(22, GPIO.HIGH)


# Drive the motor backward
def backward():
    # Motor A:

    GPIO.output(3, GPIO.HIGH) # Set AIN1

    GPIO.output(5, GPIO.LOW) # Set AIN2

    # Motor B:

    GPIO.output(7, GPIO.HIGH) # Set BIN1

    GPIO.output(11, GPIO.LOW) # Set BIN2

    # Motor C:

    GPIO.output(29, GPIO.HIGH) # Set AIN1

    GPIO.output(31, GPIO.LOW) # Set AIN2

    # Motor D:

    GPIO.output(36, GPIO.HIGH) # Set AIN1

    GPIO.output(38, GPIO.LOW) # Set AIN2

    # Set the motor speed

    GPIO.output(12, GPIO.HIGH) # Set PWMA
    
    GPIO.output(13, GPIO.HIGH) # Set PWMB
    
    GPIO.output(18, GPIO.HIGH) # Set PWMA
    
    GPIO.output(19, GPIO.HIGH) # Set PWMB
    
    GPIO.output(22, GPIO.HIGH)


def stop():
    GPIO.output(22, GPIO.LOW) # Set STBY 

    GPIO.output(5, GPIO.LOW) # Set AIN1

    GPIO.output(3, GPIO.LOW) # Set AIN2

    GPIO.output(12, GPIO.LOW) # Set PWMA

    GPIO.output(7, GPIO.LOW) # Set BIN1

    GPIO.output(11, GPIO.LOW) # Set BIN2

    GPIO.output(13, GPIO.LOW) # Set PWMB

      
 
    GPIO.output(31, GPIO.LOW) # Set AIN1

    GPIO.output(29, GPIO.LOW) # Set AIN2

    GPIO.output(18, GPIO.LOW) # Set PWMA

    GPIO.output(36, GPIO.LOW) # Set BIN1

    GPIO.output(38, GPIO.LOW) # Set BIN2

    GPIO.output(19, GPIO.LOW) # Set PWMB
    
def rotateRight():

    # Motor A:

    GPIO.output(3, GPIO.LOW) # Set AIN1

    GPIO.output(5, GPIO.HIGH) # Set AIN2

    # Motor B:
    GPIO.output(7, GPIO.LOW) # Set BIN1

    GPIO.output(11, GPIO.HIGH) # Set BIN2

    # Motor C:

    GPIO.output(29, GPIO.HIGH) # Set AIN1

    GPIO.output(31, GPIO.LOW) # Set AIN2

    # Motor D:

    GPIO.output(36, GPIO.HIGH) # Set AIN1

    GPIO.output(38, GPIO.LOW) # Set AIN2

    # Set the motor speed

    GPIO.output(12, GPIO.HIGH) # Set PWMA

    GPIO.output(13, GPIO.HIGH) # Set PWMB

    GPIO.output(18, GPIO.HIGH) # Set PWMA

    GPIO.output(19, GPIO.HIGH) # Set PWMB

    GPIO.output(22, GPIO.HIGH)
    
    
def rotateLeft():

    # Motor A:

    GPIO.output(3, GPIO.HIGH) # Set AIN1

    GPIO.output(5, GPIO.LOW) # Set AIN2

    # Motor B:

    GPIO.output(7, GPIO.HIGH) # Set BIN1

    GPIO.output(11, GPIO.LOW) # Set BIN2

    # Motor C:

    GPIO.output(29, GPIO.LOW) # Set AIN1

    GPIO.output(31, GPIO.HIGH) # Set AIN2

    # Motor D:

    GPIO.output(36, GPIO.LOW) # Set AIN1

    GPIO.output(38, GPIO.HIGH) # Set AIN2

    # Set the motor speed

    GPIO.output(12, GPIO.HIGH) # Set PWMA

    GPIO.output(13, GPIO.HIGH) # Set PWMB

    GPIO.output(18, GPIO.HIGH) # Set PWMA

    GPIO.output(19, GPIO.HIGH) # Set PWMB

    GPIO.output(22, GPIO.HIGH)
    

setup ()
rotateRight()
time.sleep(0.2)
stop()

