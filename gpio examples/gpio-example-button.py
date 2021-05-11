# Connect a button and print a message if the button is pressed

from time import sleep
from gpiozero import Button

button = Button(9)

while True:
    if button.is_pressed:
        print('hello')
    
    sleep(0.1)