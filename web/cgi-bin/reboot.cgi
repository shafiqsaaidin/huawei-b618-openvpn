#!/bin/sh
# Script Created by Jerome Laliag <jeromelaliag@yahoo.com>

echo HTTP/1.1 301 Moved Permanently
echo Location: /
echo Content-type: text/plain
echo
case "$REQUEST_METHOD" in
POST)
(
reboot
)
;;
*)
esac