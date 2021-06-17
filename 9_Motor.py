#This is Motor Program

from gpiozero import Motor
from time import sleep

motor = Motor(forward=7, backward=8)

motor.forward()
sleep(5)
motor.backward()
sleep(5)
motor.stop()
