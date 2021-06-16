# This is a User input Program

from gpiozero import LED
from time import sleep

print('''
Which number of LED you want to blink
1:red
2:blue
3:green
''')

#take input from user
led_input = int(input("Enter your option: "))

if(led_input == 1):
    led=LED(17) #Define GPIO17 as red led
if(led_input == 2):
    led=LED(27) #Define GPIO27 as blue led
if(led_input == 3):
    led=LED(22) #Define GPIO22 as green led

#take count input from user
count = int(input("How many times you want to blink led: "))

while count > 0:
    led.on() #LED ON
    sleep(0.5) #0.5s delay
    led.off() #LED OFF
    sleep(0.5) #0.5s delay
    count = count - 1 #decrease count
