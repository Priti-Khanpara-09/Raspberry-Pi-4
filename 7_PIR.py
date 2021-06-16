#This is PIR Sensor Program

from gpiozero import MotionSensor, LED

pir = MotionSensor(4) #Define GPIO4 as PIR
led = LED(17) #Define GPIO17 as LED

pir.when_motion = led.on
pir.when_no_motion = led.off
