#!/bin/sh
# Script Created by Jerome Laliag <jeromelaliag@yahoo.com>

FIND=`cat /system/etc/autorun.sh | grep /system/vpn/bin/startup.sh`
if [ -n "$FIND" ]; then
sleep 0
else
mount -o remount,rw /system /system
echo /system/vpn/bin/startup.sh >> /system/etc/autorun.sh
fi
echo Install finish!
sleep 1
echo Rebooting...
atc AT^RESET > /dev/null 2>&1