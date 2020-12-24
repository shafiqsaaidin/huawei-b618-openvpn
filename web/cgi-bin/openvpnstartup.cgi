#!/bin/sh
# Script Created by Jerome Laliag <jeromelaliag@yahoo.com>

echo Content-type: text/plain
echo
CHECK=`grep /system/vpn/web/cgi-bin/connect.cgi /system/vpn/bin/startup.sh`
if [ -n "$CHECK" ]; then
echo "<input type='button' onclick='javascript:removeopenvpnstartup()' value='Disable'>"
else
echo "<input type='button' onclick='javascript:addopenvpnstartup()' value='Enable'>"
fi