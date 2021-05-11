from time import sleep
from gpiozero import Button

button = Button(9)



while True:
    # Only sample distance on button-press
    if button.is_pressed:
        print('hello')
    
    sleep(0.1)