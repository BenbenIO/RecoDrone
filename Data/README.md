# Data

**I will make the data available on Box, once the POC is finished.**

## Presentation

As we are working with audio data, the dataset is consitued of *.wav* files, and organised into folder by categories.
Organization example:
```
data
├── armed
│   ├── 10.wav
│   ├── 1.wav
│   ├── 2.wav
│   ├── 3.wav
│   ├── 4.wav
│   ├── 5.wav
│   ├── 6.wav
│   ├── 7.wav
│   ├── 8.wav
│   └── 9.wav
└── background
    ├── 10.wav
    ├── 1.wav
    ├── 2.wav
    ├── 3.wav
    ├── 4.wav
    ├── 5.wav
    ├── 6.wav
    ├── 7.wav
    ├── 8.wav
    └── 9.wav
```

## Acquisition

You can get new data with the [Record_Audio.py](Record_Audio.py) file:
```
python Record_Audio.py.py -s 6 -n armed/06.wav
```
Make sure microphone is connected, ask for assistance if needed. It is using [PyAudio](https://pypi.org/project/PyAudio/) to interface with the Webcam.

## Other
if you have any recommandation, on how to get better training data (sample_rate, microphone, ...) please share :D