#!/usr/bin/python
import time
import pyupm_grove   # Get the UPM library

# Create the temperature sensor object
temp = pyupm_grove.GroveTemp(1)

# Use "value" method on it to get the temperature
for i in range(1,10):
        print "Temperature now is " + str(temp.value() * (9/5) + 32)
        time.sleep(1)

