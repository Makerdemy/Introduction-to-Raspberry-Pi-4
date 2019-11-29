from gpiozero import Motor
from time import sleep

motor = Motor(forward=4, backward=14)


motor.forward()
sleep(5)
motor.backward()
sleep(5)
motor.stop()
sleep(5)
motor.backward()
sleep(5)
