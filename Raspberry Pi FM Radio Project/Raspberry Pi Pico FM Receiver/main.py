from machine import Pin, I2C
#from gpio_lcd import GpioLcd
import time

push1 = Pin(10, Pin.IN, Pin.PULL_UP)
push2 = Pin(11, Pin.IN, Pin.PULL_UP)


frec = 89.0
#frec = 92.7
frec1 = 92
frec2 = 7
std1 = 1
std2 = 1

i2c = I2C(1,scl=Pin(15), sda=Pin(14), freq=400000)

time.sleep_ms(10)

def radio_frequency(freq):
    freqB = 4 * (freq * 1000000 + 225000) / 32768
    buf = bytearray(5)
    buf[0] = int(freqB) >> 8
    buf[1] = int(freqB) & 0XFF
    buf[2] = 0X90
    buf[3] = 0X1E
    buf[4] = 0X00
   #i2c.writeto(0x60, buf)
    i2c.writeto(0x60, buf)
    time.sleep_ms(10)
    
radio_frequency(frec)
