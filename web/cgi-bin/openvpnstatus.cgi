#!/bin/sh
# Script Created by Jerome Laliag <jeromelaliag@yahoo.com>

echo Content-type: text/plain
echo
OPENVPNSTATUS=`busyboxx pgrep openvpn`
if [ -n "$OPENVPNSTATUS" ]; then
echo Running
else
echo Not running
fi