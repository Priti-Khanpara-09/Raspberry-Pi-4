from gpiozero import LED
from time import sleep

led = LED(17)

while True:
    led.on() # LED ON
    sleep(1) # Sleeping for one second
    led.off()# LED OFF
    sleep(1)