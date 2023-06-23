from machine import Pin, I2C
#from gpio_lcd import GpioLcd
import time

push1 = Pin(10, Pin.IN, Pin.PULL_UP)
push2 = Pin(11, Pin.IN, Pin.PULL_UP)

#default frequency is hard set to 89.0, but you can change it
frec = 89.0

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

#setup the pin buttons
left_button = Pin(2,Pin.IN, Pin.PULL_DOWN)
right_button = Pin(3, Pin,IN, Pin.PULL_DOWN)

while True:
    #check if the state of the left button
    #changes station frequency down if left button is pressed
    #changes frequency up if the right button is pressed
    if left_button.value():
        print("-------------------------")
        print("")
        print("Changing Station Down")
        frec = frec-0.1
        radio_frequency(frec)
        print(frec)
        print("")
        print("--------------------------")
    if right_button.value():
        print("--------------------------")
        print("")
        print("Changing Station Up")
        frec = frec + 0.1
        radio_frequency(frec)
        print(frec)
        print("")
        print("--------------------------")
    #Wait for a short time to avoid constantly checking the buttons
    time.sleep(0.1)
