# Scanner i2c en MicroPython | MicroPython i2c scanner

import machine
i2c = machine.I2C(0, scl=machine.Pin(21), sda=machine.Pin(20))

print("--------- Start of Program ---------")
print('Scan i2c bus...')
devices = i2c.scan()

if len(devices) == 0:
    print("No i2c device !")
else:
    print('i2c devices found:',len(devices))

    for device in devices:  
        print("Decimal address: ",device," | Hexa address: ",hex(device))

print("---------- End of Program ----------")