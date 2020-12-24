#!/bin/sh
# Script Created by Jerome Laliag <jeromelaliag@yahoo.com>

echo Content-type: text/plain
echo
CHECK=`grep /system/vpn/web/cgi-bin/connect.cgi /system/vpn/bin/startup.sh`
if [ -n "$CHECK" ]; then
busyboxx sed -i '/connect/d' /system/vpn/bin/startup.sh
echo Success.
else
echo No OpenVPN on startup.
fi