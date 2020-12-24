#!/bin/sh
# Script Created by Jerome Laliag <jeromelaliag@yahoo.com>

echo Content-type: text/plain
echo
FINDPROCESS=`busyboxx pgrep openvpn`
if [ -n "$FINDPROCESS" ]; then
echo "<input type='button' onclick='javascript:disconnect()' value='Disconnect'>"
else
echo "<input type='button' onclick='javascript:connect()' value='Connect'>"
fi