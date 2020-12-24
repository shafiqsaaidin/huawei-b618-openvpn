#!/bin/sh
# Script Created by Jerome Laliag <jeromelaliag@yahoo.com>

echo Content-type: text/plain
echo
VPNSTATUS=`ifconfig tun0`
if [ -n "$VPNSTATUS" ]; then
echo Connected
else
echo Disconnected
fi