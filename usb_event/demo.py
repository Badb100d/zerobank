#!/usr/bin/env python
#coding:utf8

import glib
#from gi.repository import GLib as glib

from pyudev import Context, Monitor
from subprocess import Popen as popen

_DEBUG = False
g_dev_dict = {}

try:
    from pyudev.glib import MonitorObserver

    def device_event(observer, device):
        if _DEBUG:
            print 'event {0} on device {1}'.format(device.action, device)
        event_proc(device.action, device)
except Exception:
    from pyudev.glib import GUDevMonitorObserver as MonitorObserver

    def device_event(observer, action, device):
        if _DEBUG:
            print 'event {0} on device {1}'.format(action, device)
        event_proc(action, device)

def verbose_info(device):
    print 'device.device_path:\t',device.device_path
    print 'device.sys_path:\t',device.sys_path
    print 'device.sys_name:\t',device.sys_name
    print 'device.sys_number:\t',device.sys_number
    print
    for key in device.keys():
        print key,'\t',device[key]
    print '\n'

def event_proc(action, device):
    global g_dev_dict
    # 只响应设备绑定事件
    if u'bind' == action:
        if _DEBUG:
            verbose_info(device)
        # 只响应 DRIVER 为usb 的事件 //(usbfs, ipheth)
        if u'DEVTYPE' in device and device[u'DEVTYPE'] == u'usb_device':
            dev_name     = device[u'DEVNAME']
            dev_serial   = device[u'ID_SERIAL_SHORT']
            dev_model    = device[u'ID_MODEL']
            dev_string   = device[u'ID_MODEL_FROM_DATABASE'] if dev_model == u'iPhone' else device[u'ID_SERIAL']
            if dev_name in g_dev_dict:
                print dev_serial, u'already triggered'
            else:
                g_dev_dict[dev_name] = (dev_serial, dev_model, dev_string)
                print dev_serial,dev_string,u'added'
                if dev_model == u'iPhone':
                    # iphone backup
                    popen(['./ios.sh',])
                else:
                    # android adb operation
                    popen(['./android.sh',])

    elif u'unbind' ==  action:
        if _DEBUG:
            verbose_info(device)
        if u'DEVTYPE' in device and device[u'DEVTYPE'] == u'usb_device':
            dev_name = device[u'DEVNAME']
            if dev_name in g_dev_dict:
                tmp_serial, tmp_model, tmp_string = g_dev_dict.pop(dev_name)
                print tmp_serial, tmp_string, u'removed'
            else:
                print dev_name,u'not exists.'


def main():
    context = Context()
    monitor = Monitor.from_netlink(context)
    
    monitor.filter_by(subsystem='usb')
    observer = MonitorObserver(monitor)
    
    observer.connect('device-event', device_event)
    monitor.start()
    
    glib.MainLoop().run()

if '__main__' == __name__:
    main()
