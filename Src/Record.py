# Record Camera and LED

import threading
import time
import cv2
import os

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD) # PIN as numbered on the board.

class Camera:
    def __init__(self, src=0, saving_directory="../Video/"):
        # Video parameters
        self.fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        self.recording = False
        self.thread = None
        self.vid_name = "init_name.mp4"
        self.saving_directory = saving_directory
        self.check_directory()
        self.out = None

        # Get camera - Using default camera settings
        self.cap = cv2.VideoCapture(src)
        self.width = self.cap.get(3)
        self.height = self.cap.get(4)
        self.fps = self.cap.get(5)
        print("Getting video: {} ({}/{}) at {} fps.".format(src, self.width, self.height, self.fps))

    def check_directory(self):
        # Check if saving directory exist, create if not.
        if not os.path.isdir(self.saving_directory):
            os.makedirs(self.saving_directory)
            return(True)
        else:
            return(False)

    def record_loop(self):
        # Main loop for recording
        print("Starting recording {}".format(self.vid_name))
        while self.recording:
            # Get frame:
            ret, frame = self.cap.read()

            # write to out:
            self.out.write(frame)

        # Finishing recording
        self.out.release()

    def record(self, name="test_name.mp4"):
        if self.recording:
            print("[!] Already recording; {}".format(self.vid_name))

        else:
            self.vid_name = name
            self.recording = True
            self.out = cv2.VideoWriter(self.vid_name, self.fourcc, self.fps, (int(self.width), int(self.height)))
            self.thread = threading.Thread(target=self.record_loop)
            self.thread.start()

    def stop(self):
        # Stop the main thread
        self.recording = False
        self.thread.join()

class LED:
    def __init__(self, PIN_LED=8, T=0.8):
        self.PIN_LED = PIN_LED
        self.T = T
        self.blinking = False
        self.thread = None

        # Set the pin
        GPIO.setup(self.PIN_LED, GPIO.OUT)
        print("Recording LED ready.")

    def blinking_loop(self):
        # Main blinking loop
        self.blinking = True

        while self.blinking:
            GPIO.output(self.PIN_LED, GPIO.HIGH)
            time.sleep(self.T)
            GPIO.output(self.PIN_LED, GPIO.LOW)
            time.sleep(self.T)

        # Reset LED
        GPIO.output(self.PIN_LED, GPIO.LOW)

    def blink(self):
        # Start blinking thread
        if not self.blinking:
            self.thread = threading.Thread(target = self.blinking_loop)
            self.thread.start()

    def stop(self):
        # Stop blinking thread
        self.blinking = False
        self.thread.join()

    def set_T(self, new_T):
        # Set blinking period [s]
        if float(new_T) > 0:
            self.T = new_T
            print("LED - New blinking period: {} s.".format(self.T))
        else:
            print("[!] Invalide T value: {} second".format(new_T))

    def get_T(self):
        return(self.T)