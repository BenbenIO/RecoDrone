#!/bin/bash
# Start DroneReco at boot
source /home/pi/.zshrc
sleep 2

# Goto diretory
cd /home/pi/Documents/Src/
sleep 1

# Start script into log file
python DroneReco.py -m dev_model.tflite > DroneReco.log

