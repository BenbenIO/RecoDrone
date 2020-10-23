# RecoDrone
Record Drone Test is a simple project to automatically record test video of drone.

![git_from_video](Video/flight_test.gif)

## Motivation

> Tired of having to manage the RC controls / 2-3 terminals and a camera during your development ??!

With RecoDrone, just powered your RPi and a simple NeuralNetwork will detect when a drone is arm and start recording.
A blinking LED will indicate that the recording is ongoing. Then, you can download the video on the ```ftp://RPi_domainename```, and start analysis and reporting.

Video review for drone development is a real advantage and can lead to faster improvement and better reporting.
However it also require some attention, focus and time. The proposed solution aims to automate the acquisition process by starting recording video based on sound.
Indeed, a drone armed is really distincs sound and can be used to train model that will trigger the recording.

Such system can:
- Automate the test recording.
- Help development by having video analyse data.
- Provide additionnal material for report and project communication.
- Help learning more about AI on Edge and sound processing.


## Setup

<p align="center">
  <img src="Others/DroneRecoImg.jpg">
</p>

#### Hardware

- Raspberry Pi 3B+ with large SD card *(128Gb)*.
- Camera with Microphone: [BUFFALO - BSW180ABK*](https://www.buffalo.jp/product/detail/bsw180abk.html)
- Power supply.
- Basic LED, 330Ohm resistance and a bit a cable *(Optional)*
- RPi casing *(Optional)*



**Note:** I used this camera because it was lying around, have a microphone integrated and the **180deg** FoV match the application to capture the drone. I would like to test out other microphone and camera, so please feel free to give your feedback on the hardware.

#### Software
The setup on the RPi can be troublesome (good version of *librosa* so please be patient).You can also check the requirements:
- For training:

You can set your training environment with conda via:
```
conda env create -f RecoDroneConda.yml
```

- For the Pi:
```
pip install -r requirements_pi.txt
```
with *scipy* and *tflite-runtime* installed from .whl

## Porject Structure

#### - Data

Where to get, store and data acquisition script.

#### - Notebook
Data exploration and training related notebooks.

#### - Src
Code and script running on the Raspberry Pi.

#### - Other
Additionnal setup: start at boot / FTPserver / Zipping-cleaning script / ...

## Other

#### Casing
I design a specific casing that feature RPi easy fixation, LED opening and fan fixation. File available in [thingiverse](https://www.thingiverse.com/thing:4612562).

<p align="center">
  <img src="Others/casing.jpg">
</p>

#### Issue and commit
Every kind of feedback are welcome. Please do not hesitate asking question and if you want to implement new features.