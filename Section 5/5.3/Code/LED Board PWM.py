from gpiozero import LEDBoard
from time import sleep


leds = LEDBoard(17, 3, pwm=True)

while True:
    leds.on()
    sleep(1)
    leds.off()
    sleep(1)
    leds.value = (0.8, 0.2)
    sleep(1)
    leds.value = (0.5, 0.9)
    sleep(1)

