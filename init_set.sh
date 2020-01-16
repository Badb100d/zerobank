#/bin/bash

echo "iwconfig wlan0 power off" >> /etc/rc.local
echo "#iw dev wlan0 set power_save off" >> /etc/rc.local
#echo "service ssh start" >> /etc/rc.local
update-rc.d ssh start
apt-get install -y vim tmux

#nohup /root/power_control/reboot_switch.sh > /dev/null &

#nohup /root/modem_start.sh > /tmp/modem.log 2>&1 &

#nohup /root/restart_notify.sh > /dev/null 2>&1 &
