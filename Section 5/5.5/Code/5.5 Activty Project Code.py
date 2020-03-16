from gpiozero import LightSensor
from gpiozero import MotionSensor
from gpiozero import OutputDevice
from time import sleep

ldr = LightSensor(18, threshold=0.2)
pir = MotionSensor(4, threshold=0.6)
relay = OutputDevice(17)

while True:
    if ldr.light_detected:
        relay.off()
        print("Day")
        sleep(0.5)
    else:
        if pir.motion_detected:
            print("Intruder detected at night")
            relay.on()
        else:
            print("Night")
        sleep(0.5)
      