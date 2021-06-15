# This is Button Practical

from gpiozero import LED, Button
from time import sleep

led = LED(17) #Define GPIO17 as LED
button = Button(27) #Define GPIO27 as Button

while True:
    if button.is_pressed:
        #print("Button is Pressed")
        led.on()
    else:
        #print("Button is not Pressed")
        led.off()
