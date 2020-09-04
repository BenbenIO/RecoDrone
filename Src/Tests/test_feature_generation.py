# Test script for feature generation on Pi
import pyaudio
import wave
import librosa
import numpy as np
import time

def extract_feature(x, sample_rate, FFT_SIZE=256):
    # Extract simple feature
    mfccs = librosa.stft(librosa.util.normalize(x), n_fft=FFT_SIZE, window='hamming')
    mfccsscaled = np.mean(mfccs.T,axis=0)
    return(mfccsscaled)

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
    ## Get Audio Stream
    audio_interface = pyaudio.PyAudio()
    usb_audio_i = find_index_usb_audio(audio_interface)
    form_1 = pyaudio.paInt16            #16-bit resolution
    chans = 1                           # 1 channel
    sample_rate = 44100                 # 44.1kHz sampling rate
    chunk = 1*sample_rate               # 2^12 samples for buffer

    print("Audio parameters:")
    print(" {} | {} | {} | {} | {} | {}".format(form_1, chans, sample_rate, chunk ))
    audio_stream = audio_interface.open(format = form_1,
                                        rate = sample_rate,
                                        channels = chans,
                                        input_device_index = usb_audio_i,
                                        input = True,
                                        frames_per_buffer=chunk)
    print("# Audio ready.")

    # Main Loop
    audio_stream.start_stream()

    try:
        while True:
            data = np.fromstring(audio_stream.read(chunk),
                                dtype=np.int16)

            # Pause the audio stream
            audio_stream.stop_stream()

            start = time.time()

            feature = extract_feature(data, sample_rate)

            elapsed_time = time.time() - start
            print("Feature {} extracted in {}".format(feature.shape, elapsed_time))

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
