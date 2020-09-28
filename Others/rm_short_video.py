# Simple script to remove short video and remove empty directory.
import os
import config
from pathlib import Path

def get_size(mp4_file):
    # Return file size in MB
    size_in_bytes = os.path.getsize(mp4_file)
    return(size_in_bytes/(1024*1024))

def removeEmptyFolders(path):
    # Function to remove empty folders
    if not os.path.isdir(path):
        return

    files = os.listdir(path)
    if len(files):
        for f in files:
            fullpath = os.path.join(path, f)
            if os.path.isdir(fullpath):
                removeEmptyFolders(fullpath)

    # if folder empty, delete it
    files = os.listdir(path)
    if len(files) == 0:
        print("Removing empty folder: {}".format(path))
        os.rmdir(path)

def main():
    # Get config
    video_full_path = config.config.video_full_path
    min_size = config.config.min_size
    delete_cnt = 0
    print("Running video Size filtering:")
    print("  Path: {}".format(video_full_path))
    print("  Minimun size: {} MB.\n".format(min_size))

    # Removing short video
    for path in Path(video_full_path).rglob('*.mp4'):
        size_MB = get_size(path)
        if size_MB < min_size:
            os.remove(path)
            delete_cnt += 1
            print("Removed {} - {} MB".format(path.name, size_MB))
    print("Removed {} video.".format(delete_cnt))

    # Removing empty directory
    removeEmptyFolders(video_full_path)

if __name__ == "__main__":
    main()
