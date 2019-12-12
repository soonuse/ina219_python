# INA219 driver
INA219 sensor driver based on smbus.
Tested on Jetson Nano
Adafruit gives another python code for INA219, Adafruit_CircuitPython_INA219,
I appreciate their code but the dependencies are not easy to handle.
On my case, I just want the module working on smbus.
That's the reason why I rewrote the driver according to Adafruit_INA219
but not Adafruit_CircuitPython_INA219.
