import RPi.GPIO as GPIO
import time

PIN_RED = 22
PIN_GREEN = 27
PIN_TRIGGER = 26
PIN_ECHO = 19

def start():
    GPIO.setwarnings(False)
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)

    # setup leds
    GPIO.setup(PIN_RED,GPIO.OUT)
    GPIO.setup(PIN_GREEN,GPIO.OUT)
    GPIO.output(PIN_RED, GPIO.LOW)
    GPIO.output(PIN_GREEN, GPIO.LOW)
   
    # setup ultrasonic sensor
    GPIO.setup(PIN_TRIGGER, GPIO.OUT)
    GPIO.setup(PIN_ECHO, GPIO.IN)
    
def calculateDistance():

    # calculate distance
    GPIO.output(PIN_TRIGGER, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(PIN_TRIGGER, GPIO.LOW)
    
    pulse_start_time = 0
    pulse_end_time = 0
    
    while GPIO.input(PIN_ECHO)==0:
        pulse_start_time = time.time()
    while GPIO.input(PIN_ECHO)==1:
        pulse_end_time = time.time()

    pulse_duration = pulse_end_time - pulse_start_time

    distance = round(pulse_duration * 17150, 2)

    return distance
# function for turning on red LED
def turnOnRed():
    GPIO.output(PIN_RED, GPIO.HIGH)
    GPIO.output(PIN_GREEN, GPIO.LOW) 

# function for turning on green LED
def turnOnGreen():
    GPIO.output(PIN_GREEN, GPIO.HIGH)
    GPIO.output(PIN_RED, GPIO.LOW)
