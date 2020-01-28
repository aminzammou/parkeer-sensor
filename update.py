import connectie as con
import parkeer1 as sensor1
import connectie2 as con2
import parkeer2 as sensor2
import time

while True:
    dis = sensor1.calculateDistance()
    if dis < 20:
        plek = 0
    else:
        plek = 1
   
    dis2 = sensor2.calculateDistance()
    if dis2 < 20:
        plek2 = 0
    else:
        plek2 = 1
        
    time.sleep(1)
    sensor1.uitvoer()
    time.sleep(1)
    con.update()
    time.sleep(1)
    
    GPIO.cleanup()
    
    sensor2.uitvoer()
    time.sleep(1)
    con2.update()
    time.sleep(1)
    