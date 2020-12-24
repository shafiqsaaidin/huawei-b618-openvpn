#!/bin/sh
# Script Created by Jerome Laliag <jeromelaliag@yahoo.com>

echo Content-type: text/plain
echo
dl=`cat /sys/class/net/tun0/statistics/rx_bytes`
ul=`cat /sys/class/net/tun0/statistics/tx_bytes`
if [ -n "$dl" ]; then
sleep 1
down=`cat /sys/class/net/tun0/statistics/rx_bytes`
up=`cat /sys/class/net/tun0/statistics/tx_bytes`
echo Download: $((($down-$dl)/(1*1024))) KiB / $(ifconfig tun0 | grep bytes | awk '{print $3, $4}' | busyboxx tr -d '()')
echo "<br/>"
echo Upload: $((($up-$ul)/(1*1024))) KiB / $(ifconfig tun0 | grep bytes | awk '{print $7, $8}' | busyboxx tr -d '()')
else
echo Download: 0 KiB / 0.0 B
echo "<br/>"
echo Upload: 0 KiB / 0.0 B
fi