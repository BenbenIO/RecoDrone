"""
    Script to record audio from USB camera:
    run with:
    python test_record_audio.py -s 6 -n test.wav
"""

import pyaudio
import wave
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
    parser.add_argument('-n','--name', help='Name to save', dest='wav_name', default='test_acq.wav')
    parser.add_argument('-s','--sec', help='Record time [s]', dest='secs', default=5)
    args = parser.parse_args()

    # PyAudio module
    audio = pyaudio.PyAudio()

    # Acquisition parameters
    usb_audio_i = find_index_usb_audio(audio)
    form_1 = pyaudio.paInt16        #16-bit resolution
    chans = 1                       # 1 channel
    samp_rate = 44100               # 44.1kHz sampling rate
    chunk = 4096                    # 2^12 samples for buffer
    record_secs = args.secs         # seconds to record
    wav_out = args.wav_name         # name of .wav file
    
    print("Stream parameters:")
    print(" {} | {} | {} | {} | {} | {}".format(form_1, chans, samp_rate, chunk, record_secs, wav_out))
    stream = audio.open(format = form_1,
                        rate = samp_rate,
                        channels = chans,
                        input_device_index = usb_audio_i,
                        input = True,
                        frames_per_buffer=chunk)
    print("recording...")

    # Get data as array:
    frames = []
    for ii in range(0, int((samp_rate/chunk)*record_secs)):
        data = stream.read(chunk)
        frames.append(data)

    print("... Finished.")
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Write .wav file:
    wavefile = wave.open(wav_out, 'wb')
    wavefile.setnchannels(chans)
    wavefile.setsampwidth(audio.get_sample_size(form_1))
    wavefile.setframerate(samp_rate)
    wavefile.writeframes(b''.join(frames))
    wavefile.close()

if __name__ == "__main__":
    main()
