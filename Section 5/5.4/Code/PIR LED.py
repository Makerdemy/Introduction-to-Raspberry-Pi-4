from gpiozero import MotionSensor, LED
from time import sleep

pir = MotionSensor(4, threshold=0.6)
led = LED(17)

    
while True:
    if pir.motion_detected:
        print("Motion detected")
        led.on()
        sleep(0.5)
    else:
        print("No Motion")
        led.off()
        sleep(0.5)


