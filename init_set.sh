#/bin/bash

sed -i "s/exit\s0/iwconfig wlan0 power off\nexit 0/" /etc/rc.local
#sed -i "s/exit\s0/iw dev wlan0 set power_save off\nexit 0/" /etc/rc.local

#sed -i "s/exit\s0/service ssh start\nexit 0/" /etc/rc.local
update-rc.d ssh start
apt-get install -y vim tmux

#nohup /root/power_control/reboot_switch.sh > /dev/null &

#nohup /root/modem_start.sh > /tmp/modem.log 2>&1 &

#nohup /root/restart_notify.sh > /dev/null 2>&1 &
