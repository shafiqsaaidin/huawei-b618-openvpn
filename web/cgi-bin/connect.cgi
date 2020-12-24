#!/bin/sh
# Script Created by Jerome Laliag <jeromelaliag@yahoo.com>

echo Content-type: text/plain
echo
CHECK=`cat /system/vpn/config/set.txt`
if [ -n "$CHECK" ]; then
OPENVPN=`busyboxx pgrep openvpn`
if [ -n "$OPENVPN" ]; then 
echo OpenVPN is running.
else
CHECKAUTH=`grep auth-user-pass /system/vpn/config/openvpn.ovpn`
if [ -n "$CHECKAUTH" ]; then
busyboxx nice -n -20 /system/vpn/bin/openvpn --daemon --config /system/vpn/config/openvpn.ovpn --log /system/vpn/web/logs.txt --nice -20 --auth-retry interact --auth-user-pass /system/vpn/config/openvpn.auth
ebtables -t nat -D PREROUTING -p IPv4 --logical-in br0 --mark 0x0/0xff000000 -j mark --mark-or 0x10000000 --mark-target ACCEPT 2> /dev/null
else
busyboxx nice -n -20 /system/vpn/bin/openvpn --daemon --config /system/vpn/config/openvpn.ovpn --log /system/vpn/web/logs.txt --nice -20
ebtables -t nat -D PREROUTING -p IPv4 --logical-in br0 --mark 0x0/0xff000000 -j mark --mark-or 0x10000000 --mark-target ACCEPT 2> /dev/null
fi
fi
else
echo Please set or save the openvpn configuration first.
fi