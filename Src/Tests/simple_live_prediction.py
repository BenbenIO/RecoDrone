# Test script for feature generation on Pi
import pyaudio
import wave
import librosa
import numpy as np
import tflite_runtime.interpreter as tflite
import time
import argparse

DRONE_STATE = ['DISARMED',
                'ARMED']

def extract_feature(x, FFT_SIZE=256):
    # Extract simple feature (abs to get the magnetude)
    mfccs = librosa.stft(librosa.util.normalize(x), n_fft=FFT_SIZE, window='hamming')
    mfccs = np.abs(mfccs)
    feat = np.mean(mfccs.T,axis=0)
    return(np.array([feat]))

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
    ## Model file
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--model', help="Model file (.tflite)", dest='model_file', required=True)
    args = parser.parse_args()
    print("Loading {}.".format(args.model_file))

    interpreter = tflite.Interpreter(model_path=args.model_file)
    interpreter.allocate_tensors()
    input_details = interpreter.get_input_details()
    input_shape = input_details[0]['shape']
    output_details = interpreter.get_output_details()

    ## Get Audio Stream
    audio_interface = pyaudio.PyAudio()
    usb_audio_i = find_index_usb_audio(audio_interface)
    form_1 = pyaudio.paInt16            #16-bit resolution
    chans = 1                           # 1 channel
    sample_rate = 22050                 # 44.1kHz sampling rate
    chunk = 1*sample_rate               # 2^12 samples for buffer

    print("Audio parameters:")
    print(" {} | {} | {} | {}".format(form_1, chans, sample_rate, chunk ))
    audio_stream = audio_interface.open(format = form_1,
                                        rate = sample_rate,
                                        channels = chans,
                                        input_device_index = usb_audio_i,
                                        input = True,
                                        frames_per_buffer=chunk)
    print("\nAudio ready.")

    # Main Loop
    audio_stream.start_stream()

    try:
        while True:
            data = np.fromstring(audio_stream.read(chunk), dtype=np.int16)

            # Pause the audio stream
            audio_stream.stop_stream()
            print("\nData: {}".format(data.shape))
            start = time.time()

            # Extract feature:
            feature = extract_feature(data)

            ## TODO add feature.shape == input_shape check as test.

            interpreter.set_tensor(input_details[0]['index'], feature)
            interpreter.invoke()
            output_data = interpreter.get_tensor(output_details[0]['index'])

            elapsed_time = time.time() - start
            print("Feature ~ Inference in {} ms.".format(elapsed_time*1000))
            print("Output data: {}".format(output_data))

            ## Post processing:
            current_state = DRONE_STATE[np.argmax(output_data)]
            print("Current STATE: {}".format(current_state))

            # Resume the audio stream
            audio_stream.start_stream()

    except KeyboardInterrupt:
        print('Requested to terminate')

    finally:
        audio_stream.stop_stream()
        audio_stream.close()
        audio_interface.terminate()
        print('Terminated')

if __name__ == "__main__":
    main()
