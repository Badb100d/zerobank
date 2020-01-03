#!/usr/bin/env python3
#coding:utf8

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep
from time import time
from threading import Lock, Timer


# gpio number led_pins = [5, 6, 13, 19]
led_pins = [29, 31, 33, 35]  # physical pin number

class LED:
    def __init__(self, timeout = 30):
        self.pins = led_pins
        self.status = 0
        self.lock = Lock()
        self.upd_t = time()
        self.timeout = timeout
        for p in self.pins:
            GPIO.setup(p, GPIO.OUT)
            GPIO.output(p, GPIO.LOW)

    def set_value(self, v = 0):
        self.lock.acquire()
        v = v % 16
        self.status = v

        p = []
        p.append(v & 1)
        p.append(v & 2)
        p.append(v & 4)
        p.append(v & 8)

        for pin, value in zip(self.pins, p):
            value = GPIO.HIGH if value else GPIO.LOW
            GPIO.output(pin, value)

        self.upd_t = time()

        if not 0 == self.status:
            self.timer = Timer(self.timeout, self.fade_timer, [])
            self.timer.start()

        self.lock.release()

    def inc(self):
        v = self.status + 1
        v %= 16
        self.set_value(v)
    
    def dec(self):
        v = self.status - 1
        v %= 16
        self.set_value(v)

    def fade_timer(self):
        self.lock.acquire()
        t_delta = time() - self.upd_t
        self.lock.release()
        if t_delta >= self.timeout:
            self.set_value(0)

def main():
    GPIO.setwarnings(True) # Ignore warning for now
    GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
    led = LED()
    for i in range(16):
        sleep(1)
        print(hex(i))
        led.set_value(i)
    message = input("Press enter to quit\n\n") # Run until someone presses enter
    GPIO.cleanup() # Clean up

if '__main__' == __name__:
    main()
