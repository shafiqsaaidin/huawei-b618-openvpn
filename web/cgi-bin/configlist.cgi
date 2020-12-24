#!/bin/sh
# Script Created by Jerome Laliag <jeromelaliag@yahoo.com>

echo Content-type: text/plain
echo
SET=`cat /system/vpn/config/set.txt`
if [ -n "$SET" ]; then
echo "<select name='config'>"
echo "<option>$SET</option>"
else
echo "<select name='config'>"
fi
if [ -n "$SET" ]; then
cd /system/vpn/config/ovpn && ls *.ovpn | busyboxx sed 's/.ovpn//' | grep -Fv "$SET" | while read LIST; do
echo "<option>$LIST</option>"
done
echo "</select>"
else
cd /system/vpn/config/ovpn && ls *.ovpn | busyboxx sed 's/.ovpn//' | while read LIST; do
echo "<option>$LIST</option>"
done
echo "</select>"
fi