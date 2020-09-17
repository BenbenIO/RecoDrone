## Src [WIP]

This directory contents all source code to run on the RPi with the associated tests:

```
├── DroneReco.py
├── README.md
├── Record.py
└── Tests
    ├── simple_live_prediction.py
    ├── test_feature_generation.py
    ├── test_led.py
    ├── test_loading_model.py
    └── test_recording.py
```

### Main code:
You should be able to run the main script with:
```
python DroneReco.py -m ../Model/dev_simplefeature.tflite
```

### Test code:
To help debugging, or to integrat new features you can use the test scripts.
```
python test_*****.py -** *******
```

Currently no integration to any MicroTest framework. But would like to have some help on that.