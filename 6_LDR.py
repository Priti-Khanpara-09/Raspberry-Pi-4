#This is Light Dependent Resistor (LDR) Program

from gpiozero import LightSensor

ldr = LightSensor(17) #Define GPIO17 as LDR
'''
while True:
    ldr.wait_for_light()
    print("It's Light :)")
    ldr.wait_for_dark()
    print("It's Dark :(")
'''
#Let's print ldr value
while True:
    print(ldr.value)
