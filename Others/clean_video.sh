#!/bin/bash
# Script to clean video folder: rm short_video / empty directory
# Specify Video directory in config.py

source /home/pi/.zshrc
sleep 1
cd /home/pi/Documents/Others
sleep 1
python rm_short_video.py >> removed.log 2>&1
echo Clean Video
