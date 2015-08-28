#!/bin/sh
DIR=`sudo find / -type d -name py3status`/modules
sudo cp airvpn_status.py $DIR
sudo cp airvpn_api.key $DIR
sudo cp airvpn_i3.py $DIR/airvpn.py
