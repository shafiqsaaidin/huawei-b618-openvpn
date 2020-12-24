#!/bin/sh
# Script Created by Jerome Laliag <jeromelaliag@yahoo.com>

FIND=`cat /system/etc/autorun.sh | grep /system/vpn/bin/startup.sh`
if [ -n "$FIND" ]; then
mount -o remount,rw /system /system
busyboxx sed -i -e '/\/system\/vpn\/bin\/startup.sh/d' /system/etc/autorun.sh
fi
rm -rf /system/vpn/
echo Uninstall finish!
reboot