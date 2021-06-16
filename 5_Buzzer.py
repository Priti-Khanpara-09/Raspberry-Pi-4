from gpiozero import Buzzer
from time import sleep

buzzer = Buzzer(23) #Define GPIO23 as buzzer

while True:
    buzzer.on() #Buzzer ON
    sleep(0.5) #0.5s delay
    buzzer.off() #Buzzer OFF
    sleep(0.5) #0.5s delay
