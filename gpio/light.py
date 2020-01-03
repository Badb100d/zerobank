#!/usr/bin/env python3
#coding:utf8

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep


# gpio number pins = [5, 6, 13, 19]
pins = [29, 31, 33, 35]  # physical pin number

def button_callback(channel):
    print(channel,"button was pushed!")

def set_value():
    for p in pins:
        GPIO.setup(p, GPIO.OUT)
        GPIO.output(p, GPIO.LOW)
        sleep(1)

    for p in pins:
        GPIO.setup(p, GPIO.OUT)
        GPIO.output(p, GPIO.HIGH)
        print(p)
        sleep(1)


def main():
    GPIO.setwarnings(True) # Ignore warning for now
    GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
    set_value()
    message = input("Press enter to quit\n\n") # Run until someone presses enter
    GPIO.cleanup() # Clean up

if '__main__' == __name__:
    main()
