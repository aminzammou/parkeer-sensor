import parkeer1 as sensor1
import parkeer2 as sensor2
import time
import RPi.GPIO as GPIO

try:
    sensor1.uitvoer()
    sensor2.uitvoer()
        
        

except KeyboardInterrupt:
    print("Measurement stopped by User")
    GPIO.cleanup()
finally:
    GPIO.cleanup()