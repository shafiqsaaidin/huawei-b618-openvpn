#!/bin/sh
# Script Created by Jerome Laliag <jeromelaliag@yahoo.com>

mount -o remount,rw /system /system
busyboxx sysctl -w fs.file-max=51200
busyboxx sysctl -w net.core.rmem_max=67108864
busyboxx sysctl -w net.core.wmem_max=67108864
busyboxx sysctl -w net.core.netdev_max_backlog=250000
busyboxx sysctl -w net.core.somaxconn=4096
busyboxx sysctl -w net.ipv4.tcp_tw_reuse=1
busyboxx sysctl -w net.ipv4.tcp_fin_timeout=30
busyboxx sysctl -w net.ipv4.tcp_keepalive_time=1200
busyboxx sysctl -w net.ipv4.ip_local_port_range="10000 65000"
busyboxx sysctl -w net.ipv4.tcp_max_syn_backlog=8192
busyboxx sysctl -w net.ipv4.tcp_max_tw_buckets=5000
busyboxx sysctl -w net.ipv4.tcp_fastopen=3
busyboxx sysctl -w net.ipv4.tcp_mem="25600 51200 102400"
busyboxx sysctl -w net.ipv4.tcp_rmem="4096 87380 67108864"
busyboxx sysctl -w net.ipv4.tcp_wmem="4096 65536 67108864"
busyboxx sysctl -w net.ipv4.tcp_mtu_probing=1
setprop net.tcp.buffersize.default 4096,87380,256960,4096,16384,256960
setprop net.tcp.buffersize.edge 4096,87380,256960,4096,16384,256960
setprop net.tcp.buffersize.gprs 4096,87380,256960,4096,16384,256960
setprop net.tcp.buffersize.umts 4096,87380,256960,4096,16384,256960
setprop net.tcp.buffersize.wifi 4096,87380,256960,4096,16384,256960
mkdir -p /dev/net
busyboxx mknod -m 666 /dev/net/tun c 10 200
busyboxx httpd -p 8080 -c /system/vpn/bin/passwd -h /system/vpn/web/
iptables -t nat -A POSTROUTING -o tun0 -j MASQUERADE
iptables -I INPUT -i tun0 -j DROP
sleep 10
