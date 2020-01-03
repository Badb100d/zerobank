#!/bin/sh
sleep 60
while true;
do 
    /root/power_control/reboot_switch.py >/dev/null
    sleep 1
done
    
