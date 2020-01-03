#!/bin/bash

if [ -e "/dev/cdc-wdm0" ];then
    echo "cdc-wdm0 detected."
    if [ `cat /sys/class/net/wwan0/qmi/raw_ip` == 'Y' ];then
        echo "Already started."
        exit 0
    fi

    qmicli -d /dev/cdc-wdm0 --dms-get-operating-mode
    sleep 1
    qmicli -d /dev/cdc-wdm0 -w
    sleep 1
    ip link set wwan0 down
    sleep 1
    echo 'Y'|tee  /sys/class/net/wwan0/qmi/raw_ip 
    sleep 1
    ip link set wwan0 up
    sleep 1
    qmicli -p -d /dev/cdc-wdm0 --device-open-net='net-raw-ip|net-no-qos-header' --client-no-release-cid #--wds-start-network="apn='iot.njm2mapn',ip-type=4"
    sleep 1
    udhcpc -i wwan0
else
    echo "no cdc-wdm0 detect."
    exit 0
fi

