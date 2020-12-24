#!/bin/sh
# Script Created by Jerome Laliag <jeromelaliag@yahoo.com>

case "$REQUEST_METHOD" in
POST)
(
FILE=`cat`
FILENAME=`echo "$FILE" | grep filename | busybox awk -F\" '{print $4}'`
echo "$FILE" | busyboxx sed '1,4d' | busyboxx sed '$d' | busyboxx sed '$d' | busyboxx sed '$d' | busyboxx sed '$d' | busyboxx sed '$d' | busyboxx sed 's/\r$//' > "/system/vpn/config/ovpn/$FILENAME"
)
;;
*)
esac
echo HTTP/1.1 301 Moved Permanently
echo Location: /
echo Content-type: text/plain
echo