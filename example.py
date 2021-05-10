# This example will help read the temperature and light sensors
from time import sleep

# modules to read data from sensors
from PiicoDev_TMP117 import PiicoDev_TMP117
from PiicoDev_VEML6030 import PiicoDev_VEML6030

# Initialise the sensors
tempSensor = PiicoDev_TMP117()
lightSensor = PiicoDev_VEML6030()

# Loop forever
while True:
    degC = tempSensor.readTempC() # read the temperature sensor [degrees Celsius]    
    lux = lightSensor.read() # read the light sensor [lux]

    print(F'Temperature {degC:.2f} degC   Light: {lux:.0f} Lux')

    sleep(1)
