#This is Ultrasonic Sensor Program

from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(echo=24, trigger=23, max_distance=1)

while True:
    print("Distance: ", sensor.distance * 100, "cm")
    sleep(0.5) #0.5s delay
