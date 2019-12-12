from ina219 import INA219, INA219_ADDRESS

if __name__ == "__main__":
    ina219 = INA219(address=INA219_ADDRESS)
    try:
        print('bus voltage %d mV' % ina219.get_bus_voltage_mV())
    except AssertionError as e:
        print(repr(e))
        print('Retry...')
        print('bus voltage %d mV' % ina219.get_bus_voltage_mV())
    print('shunt voltage %.3f mV' % ina219.get_shunt_voltage_mV())
    print('current %.3f mA' % ina219.get_current_mA())
    print('power %.3f mW' % ina219.get_power_mW())
