#!/usr/bin/env python3
#coding:utf8

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep


#pins = [3, 5, 7, 8, 10, 11, 12, 13, 15, 16, 18, 19, 21, 22, 23, 24, 26]

pins = [ 7,] # BCM io4

def voltage_chaged(channel):
    if GPIO.LOW == GPIO.input(channel):
        #print(channel,"Voltage down!")
        print("Using battery now.")
    else:
        #print(channel,"Voltage up!")
        print("Charging battery now.")

def get_button():
    for p in pins:
        GPIO.setup(p, GPIO.IN, pull_up_down=GPIO.PUD_OFF)
        GPIO.add_event_detect(p,GPIO.BOTH,callback=voltage_chaged) # Setup event on pins rising edge

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
    voltage_chaged(pins[0])
    #set_value()
    message = input("Press enter to quit\n\n") # Run until someone presses enter
    GPIO.cleanup() # Clean up

if '__main__' == __name__:
    main()
