from time import sleep
from gpiozero import Servo

servo = Servo(9, min_pulse_width=1/2000)

while True:
    servo.value = -1 # min
    sleep(1)
    servo.value = 0 # middle
    sleep(1)
    servo.value = 1 # max
    sleep(1)