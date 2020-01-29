import connectie as con
import parkeer1 as sensor1
import connectie2 as con2
import parkeer2 as sensor2
import time
import RPi.GPIO as GPIO

while True:
    #running sensor 1 and data of sensor 1
    time.sleep(1)
    sensor1.start()
    print(sensor1.calculateDistance())
    if sensor1.calculateDistance() < 20:
        sensor1.turnOnRed()
        plek = 0
    else:
        sensor1.turnOnGreen()
        plek = 1
    
    time.sleep(1)
    con.update()
    time.sleep(1)
        
    
    #running sensor 2 and data of sensor 2
    time.sleep(1)
    sensor2.start()
    print(sensor2.calculateDistance2(), "cm")
    if sensor2.calculateDistance2() < 20:
        sensor2.turnOnRed()
        plek2 = 0
    else:
        sensor2.turnOnGreen()
        plek2 = 1
        
    time.sleep(1)
    con2.update()
    time.sleep(1)
    
    #cleans all gpio ports
    GPIO.cleanup()
        
    
    