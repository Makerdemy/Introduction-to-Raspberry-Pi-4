from gpiozero import Button, OutputDevice

relay = OutputDevice(4)
btn = Button(2)

while True:
    if btn.is_pressed:
        relay.on()
    else:
        relay.off()