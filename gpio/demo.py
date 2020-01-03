#!/usr/bin/env python3
#coding:utf8

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep


pins = [3, 5, 7, 8, 10, 11, 12, 13, 15, 16, 18, 19, 21, 22, 23, 24, 26]

def button_callback(channel):
    print(channel,"button was pushed!")

def get_button():
    for p in pins:
        GPIO.setup(p, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        #GPIO.add_event_detect(p,GPIO.RISING,callback=button_callback) # Setup event on pin 10 rising edge
        GPIO.add_event_detect(p,GPIO.FALLING,callback=button_callback) # Setup event on pin 10 rising edge

def set_value():
    for p in pins:
        GPIO.setup(p, GPIO.OUT)
        GPIO.output(p, GPIO.LOW)

    for p in pins:
        GPIO.setup(p, GPIO.OUT)
        GPIO.output(p, GPIO.HIGH)
        print(p)
        sleep(1)


def main():
    GPIO.setwarnings(True) # Ignore warning for now
    GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
    get_button()
    #set_value()
    message = input("Press enter to quit\n\n") # Run until someone presses enter
    GPIO.cleanup() # Clean up

if '__main__' == __name__:
    main()
