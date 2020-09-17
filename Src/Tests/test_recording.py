# Test script for video recording
import cv2
import time, os
import sys
sys.path.insert(0, '../')
import Record

def main():
    # Generate recording object
    reco_cam = Record.Camera(saving_directory="./")
    video_name = "test_record.mp4"
    reco_time = 10

    # Start recording:
    print("Starting recording for {} sec.".format(reco_time))
    reco_cam.record(video_name)

    time.sleep(reco_time)

    # Stop recording
    reco_cam.stop()
    time.sleep(2)
    print("Recording finished.")

    # Check if video is saved:
    files = os.listdir('.')
    if video_name in files:
        print("{} found !".format(video_name))
    else:
        print("video not saved: {}".format(files))

if __name__ == "__main__":
    main()