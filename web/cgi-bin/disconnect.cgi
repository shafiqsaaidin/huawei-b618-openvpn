#!/bin/sh
# Script Created by Jerome Laliag <jeromelaliag@yahoo.com>

echo Content-type: text/plain
echo
OPENVPN=`busyboxx pgrep openvpn`
if [ -n "$OPENVPN" ]; then 
busyboxx pkill openvpn
iptables -t nat -I POSTROUTING -o eth_x -j MASQUERADE
echo Disconnected.
else
echo OpenVPN is not running.
fi