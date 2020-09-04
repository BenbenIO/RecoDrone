"""
    Script to record audio from USB camera:
    run with:
    python test_record_audio.py -s 6 -n test.wav
"""
import tflite_runtime.interpreter as tflite
import cv2

import pyaudio
import wave
import librosa

import argparse



def find_index_usb_audio(audio, name="BUFFALO"):
    for dev_i in range(audio.get_device_count()):
        if name in audio.get_device_info_by_index(dev_i).get('name'):
            usb_audio_id = dev_i
            print("\nFound {} audio device at {}.".format(name, usb_audio_id))
            return(usb_audio_id)

        else:
            print("\n{} not found.".format(name))
            return(-1)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m','--model', help='Model file', dest='model_file', required=True)
    #parser.add_argument('-s','--sec', help='Record time [s]', dest='secs', default=5)
    args = parser.parse_args()

    ## Load model
    print("loading model: {}...".format(args.model_file))
    interpreter = tflite.Interpreter(model_path=args.model_file)

    ## Get Audio Stream
    audio = pyaudio.PyAudio()
    usb_audio_i = find_index_usb_audio(audio)
    form_1 = pyaudio.paInt16        #16-bit resolution
    chans = 1                       # 1 channel
    samp_rate = 44100               # 44.1kHz sampling rate
    chunk = 1*samp_rate             # 2^12 samples for buffer
    
    print("Audio parameters:")
    print(" {} | {} | {} | {} | {} | {}".format(form_1, chans, samp_rate, chunk ))
    stream = audio.open(format = form_1,
                        rate = samp_rate,
                        channels = chans,
                        input_device_index = usb_audio_i,
                        input = True,
                        frames_per_buffer=chunk)
    print("= Audio ready.")



if __name__ == "__main__":
    main()
