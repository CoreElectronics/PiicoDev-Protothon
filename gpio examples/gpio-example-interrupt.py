from time import sleep
from gpiozero import LED, DistanceSensor, Button

led = LED(7)
button = Button(9)
distSensor = DistanceSensor(echo=21, trigger=20)


# Define a function that prints the distance
def getDistance():
    print(distSensor.distance)

# Set the function as the button's callback
button.when_pressed = getDistance

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)

