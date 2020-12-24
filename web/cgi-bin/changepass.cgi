#!/bin/sh
# Script Created by Jerome Laliag <jeromelaliag@yahoo.com>

echo HTTP/1.1 301 Moved Permanently
echo Location: /
echo Content-type: text/plain
echo
case "$REQUEST_METHOD" in
POST)
(
FILE=`cat`
USERNAME=`echo "$FILE" | busyboxx cut -f 1 -d '&' | busyboxx cut -f 2 -d '='`
PASSWORD=`echo "$FILE" | busyboxx cut -f 2 -d '&' | busyboxx cut -f 2 -d '='`
PASSWD=`busyboxx httpd -m $PASSWORD`
echo "/:$USERNAME:$PASSWD" > /system/vpn/bin/passwd
reboot
)
;;
*)
esac