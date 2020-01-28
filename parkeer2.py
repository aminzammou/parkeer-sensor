import RPi.GPIO as GPIO
import time

PIN_RED = 24
PIN_GREEN = 23
PIN_TRIGGER =20
PIN_ECHO = 21


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
    #print("Calculating distance")

    GPIO.output(PIN_TRIGGER, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(PIN_TRIGGER, GPIO.LOW)
    while GPIO.input(PIN_ECHO)==0:
        pulse_start_time = time.time()
    while GPIO.input(PIN_ECHO)==1:
        pulse_end_time = time.time()

    pulse_duration = pulse_end_time - pulse_start_time

    distance = round(pulse_duration * 17150, 2)

    #print("Distance:",distance,"cm")
    return distance

def turnOnRed():
    GPIO.output(PIN_RED, GPIO.LOW)
    GPIO.output(PIN_GREEN, GPIO.LOW) 

def turnOnGreen():
    GPIO.output(PIN_GREEN, GPIO.HIGH)
    GPIO.output(PIN_RED, GPIO.LOW)

def uitvoer():
    start()
    distance = calculateDistance()
    if distance < 20:
        turnOnRed()
    else:
        turnOnGreen()

    print('distance ', distance)
uitvoer()