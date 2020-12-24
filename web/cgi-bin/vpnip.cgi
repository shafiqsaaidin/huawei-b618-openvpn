#!/bin/sh
# Script Created by Jerome Laliag <jeromelaliag@yahoo.com>

echo Content-type: text/plain
echo
VPNIP=`ip -4 -o addr show tun0 | busyboxx awk '{print $4}' | sed 's/\/24//g'`
if [ -n "$VPNIP" ]; then
echo "$VPNIP"
else
echo "0.0.0.0"
fi