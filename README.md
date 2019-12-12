# INA219 driver
INA219 sensor driver based on smbus.

-   Tested on Jetson Nano

Adafruit gives another python code for INA219, Adafruit_CircuitPython_INA219.

I appreciate their code but the dependencies are not easy to handle.

On my case, I just want the module working on smbus.

That's the reason why I rewrote the driver according to Adafruit_INA219
but not Adafruit_CircuitPython_INA219.

## How to use
Just try it by
```
python3 ina219_example.py
```

## Notes
-   I2C device: /dev/i2c-1 
-   INA219 address: 0x40
-   bus_voltage_range: INA219_CONFIG_BVOLTAGERANGE_32V,
-   gain: INA219_CONFIG_GAIN_8_320MV,
-   bus_adc: INA219_CONFIG_BADCRES_12BIT,
-   shunt_adc: INA219_CONFIG_SADCRES_12BIT_1S_532US,
-   mode: INA219_CONFIG_MODE_SANDBVOLT_CONTINUOUS,
-   cal_value: self.cal_value
