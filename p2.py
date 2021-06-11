from gpiozero import LED, Button

led = LED(17)
button = Button(22)

'''
while True:
    if button.is_pressed:
        led.on()
    else:
        led.off()
'''
'''
while True:
    button.wait_for_press()
    led.on()
    button.wait_for_release()
    led.off()
'''

button.when_pressed = led.on
button.when_released = led.off