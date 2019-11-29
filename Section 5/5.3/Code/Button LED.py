from gpiozero import LED, Button

led = LED(17)
button = Button(2)

    
while True:
    if button.is_pressed:
        print("Button is pressed")
        led.on()
    else:
        print("Button is not pressed")
        led.off()

