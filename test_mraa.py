#!/usr/bin/python
import mraa
import math
import time
# More info here -> http://www.seeedstudio.com/wiki/Grove_-_Temperature_Sensor_V1.2
B=3975
ain = mraa.Aio(1)
a = ain.read()
resistance = (1023-a)*10000.0/a
temp = 1/(math.log(resistance/10000.0)/B+1/298.15)-273.15
print "Temperature now is " + str(temp * 9/5 + 32)

def get_temp():
        a = ain.read()
        resistance = (1023-a)*10000.0/a
        temp = 1/(math.log(resistance/10000.0)/B+1/298.15)-273.15
        temp_msg = time.strftime("%Y-%m-%d %H:%M:%S") + " Temperature now is " + str(int(temp * 9/5 + 32)) + " degrees fahrenheit"
        return temp_msg


