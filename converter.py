import os
from moviepy.editor import *
import argparse

parser = argparse.ArgumentParser(description='MP4 TO MP3')
parser.add_argument('--mp4_dir', help='folder path for MP4 files')

args = parser.parse_args()

dest_mp3 = 'dest_mp3'
if not os.path.exists(dest_mp3):
    os.makedirs(dest_mp3)

dir = args.mp4_dir

def convert(src_file):
    video = VideoFileClip(os.path.join(dir,src_file))
    video.audio.write_audiofile(os.path.join(dest_mp3,os.path.splitext(src_file)[0]+'.mp3'))

for filename in os.listdir(dir):
    convert(filename)