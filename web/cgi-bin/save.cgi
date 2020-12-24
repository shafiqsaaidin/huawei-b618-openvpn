#!/bin/sh
# Script Created by Jerome Laliag <jeromelaliag@yahoo.com>

PRINT=`cat`
FILENAME=`echo "$PRINT" | busyboxx sed -n '4p' | busyboxx sed 's/\r$//'`
echo "$PRINT" | busyboxx sed -n '8p' | busyboxx sed 's/\r$//' > /system/vpn/config/openvpn.auth
echo "$PRINT" | busyboxx sed -n '12p' | busyboxx sed 's/\r$//' >> /system/vpn/config/openvpn.auth
cat "/system/vpn/config/ovpn/$FILENAME.ovpn" > /system/vpn/config/openvpn.ovpn
echo "$FILENAME" > /system/vpn/config/set.txt
echo HTTP/1.1 301 Moved Permanently
echo Location: /
echo Content-type: text/plain
echo