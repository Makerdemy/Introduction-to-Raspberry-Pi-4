from gpiozero import LEDBoard
from time import sleep


leds = LEDBoard(17, 3)

while True:
    leds.on()
    sleep(1)
    leds.off()
    sleep(1)
    leds.value = (1, 0)
    sleep(1)
    leds.value = (0, 1)
    sleep(1)
