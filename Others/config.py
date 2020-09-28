# Config file: use to path absolute path for the video folder
## video_full_path - String - Full path to the main Video folder.
## min_size - Int [MB] - Minimun size threshold for removing.
from easydict import EasyDict

video_full_path = "/home/ben/Documents/AI_on_Edge/Experiement_recording/rm_short_video/Video" #"/home/pi/Documents/Video"
min_size = 4

config = EasyDict()
config.video_full_path = video_full_path
config.min_size = min_size
