# This is Led Blinking Program

from gpiozero import LED
from time import sleep

led = LED(17) #define GPIO17 pin as LED

while True:
    led.on() #LED ON
    sleep(0.5) #0.5s delay
    led.off() #LED 0FF
    sleep(0.5) #0.5s delay
