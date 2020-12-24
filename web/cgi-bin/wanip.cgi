#!/bin/sh
# Script Created by Jerome Laliag <jeromelaliag@yahoo.com>

echo Content-type: text/plain
echo
WANIP=`ip -4 -o addr show eth_x  | busyboxx awk '{print $4}' | busyboxx sed -e "s/\/32//"`
if [ -n "$WANIP" ]; then
echo "$WANIP"
else
echo "0.0.0.0"
fi