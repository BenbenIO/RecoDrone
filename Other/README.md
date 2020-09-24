# Others - {WIP}

## Start at boot
The project is way more convenient if the script is running at boot. Here is how to setup simple script and run it at boot:

#### 1 - Starting script
If you install using virtualenv, you will have to activate it, then navigate to your path, and run the main script
```bash
#!/bin/bash
# Start DroneReco at boot
source /home/pi/.zshrc
sleep 2

# Goto diretory
cd /home/pi/Documents/Src/
sleep 1

# Start script into log file
python DroneReco.py -m dev_model.tflite
```

#### 2 - Generate the service
Then you have to generate a service under ```/lib/systemd/system/DroneReco.service``` as:
```bash
[Unit]
Description=Will start DroneReco
After=network.target

[Service]
ExecStart=/home/pi/DroneReco.sh
User=pi

[Install]
WantedBy=multi-user.target
```

#### 3 - Activate the service
Then you have to load and enable the service:
```
sudo systemctl daemon-reload
sudo systemctl enable DroneReco.service
```
Finally check that everything is running with ```systemclt status DroneReco.servce```

## FTP server
[WIP]

## Zipping / deleting files
[WIP]