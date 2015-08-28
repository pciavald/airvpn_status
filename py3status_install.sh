#!/bin/sh
DIR=`sudo find / -type d -name py3status`/modules
cp airvpn_status.py $DIR
cp airvpn_api.key $DIR
cp airvpn_i3.py $DIR/airvpn.py
