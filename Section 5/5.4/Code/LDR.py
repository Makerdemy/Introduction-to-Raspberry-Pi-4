from gpiozero import LightSensor
from gpiozero import LED

sensor = LightSensor(18, threshold=0.2)
led = LED(17)
    
while True:
    if sensor.light_detected:
        print("It's light! :)")
        led.on()
    else:
        print("It's dark :(")
        led.off()