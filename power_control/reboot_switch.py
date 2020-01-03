#!/usr/bin/env python3
#coding:utf8

import threading
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import logging
import os
from time import time
from PushoverSender import PushoverSender
from led import LED


g_pins = [11,]

g_event = None
g_list = []

TRIGGER_TIMES = 5

DELTA_TIME = 2.0 # seconds

g_led = None


def button_callback(channel):
    global g_list, g_event, g_led

    logging.debug('button_callback')

    #记录回调时间
    g_list.append(time())
    g_led.dec()

    if len(g_list) > TRIGGER_TIMES:
        # 超出记录长度，则删除旧记录
        g_list = g_list[-TRIGGER_TIMES:]

    # 等于记录长度
    if len(g_list) == TRIGGER_TIMES:
        # 计算多次按下的时间差，比较是否满足短时
        delta = g_list[-1] - g_list[0]
        if delta < DELTA_TIME:
            logging.debug("got signal")
            g_event.set()


def regist_button():
    # 注册pins
    for p in g_pins:
        # 初始为高电压
        GPIO.setup(p, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        
        # 按钮按下时回调按钮函数
        GPIO.add_event_detect(p,GPIO.FALLING,callback=button_callback)

def main():
    global g_event, g_led

    cwd = os.path.abspath(os.path.dirname(__file__))
    logging.basicConfig(filename=cwd+'/log.log',level=logging.DEBUG,format='%(asctime)s %(filename)s[line:%(lineno)d] %(message)s',datefmt='%Y-%m-%d %H:%M:%S')

    # 初始化 event
    g_event = threading.Event()

    # 初始化 gpio
    GPIO.setwarnings(True) # Ignore warning for now
    GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

    # 初始化 LED
    g_led = LED()
    g_led.set_value(15)

    regist_button()

    b_reboot = False
    try:
        # 等待事件触发
        g_event.wait()
        b_reboot = True

    except KeyboardInterrupt as e:
        logging.warning("KeyboardInterrupted")
        pass

    # 清理GPIO
    logging.debug("gpio cleaning")
    GPIO.cleanup() # Clean up
    logging.debug("gpio cleaned")

    if b_reboot:
        logging.debug("shutting down")
        os.system('shutdown -r 0')

if '__main__' == __name__:
    main()
