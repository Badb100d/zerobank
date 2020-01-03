#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from threading import Timer
from time import time

class demo:
    def __init__(self):
        print('init')
        self.para = '123'

    def t_thread(self):
        print('t_thread',self.para,time())

    def set_timer(self):
        self.timer = Timer(3,self.t_thread,[])

def talk(name):
    print("%s is talking." % name)


if __name__ == '__main__':
    '''Timer(等待多少秒, 执行的函数, args给函数传参数)'''
    timer = Timer(3, talk, args=("lily",))
    timer.start()
    print("main end")

