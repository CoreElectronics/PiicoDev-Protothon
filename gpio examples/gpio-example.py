from time import sleep
from gpiozero import LED, DistanceSensor, Button

led = LED(7)
button = Button(9)
distSensor = DistanceSensor(echo=21, trigger=20)


while True:
    # Only sample distance on button-press
    if button.is_pressed:
        print(distSensor.distance)
        
    led.on()
    sleep(1)
    led.off()
    sleep(1)
