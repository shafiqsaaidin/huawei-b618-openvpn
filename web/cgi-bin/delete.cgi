#!/bin/sh
# Script Created by Jerome Laliag <jeromelaliag@yahoo.com>

PRINT=`cat`
FILENAME=`echo "$PRINT" | busyboxx sed -n '4p' | busyboxx sed 's/\r$//'`
rm "/system/vpn/config/ovpn/$FILENAME.ovpn"
SET=`cat /system/vpn/config/set.txt`
if [ "$SET" = "$FILENAME" ]; then 
rm "/system/vpn/config/set.txt"
fi
echo HTTP/1.1 301 Moved Permanently
echo Location: /
echo Content-type: text/plain
echo