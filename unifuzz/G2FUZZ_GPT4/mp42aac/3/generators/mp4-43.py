import cv2
import numpy as np
import os
import subprocess  # More secure way to call external commands

# Ensure tmp directory exists
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Video settings
width, height = 640, 480
fps = 24
codec = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for .mp4 files
video_filename = './tmp/sample_video_advanced_features.mp4'

# Create VideoWriter object
out = cv2.VideoWriter(video_filename, codec, fps, (width, height))

# Generate video content (A simple animation of a moving white square on a black background)
num_frames = 120  # 5 seconds of video at 24 fps
for i in range(num_frames):
    frame = np.zeros((height, width, 3), np.uint8)  # Black background
    cv2.rectangle(frame, (10 + i*5, 50), (60 + i*5, 100), (255, 255, 255), -1)  # Moving white square
    out.write(frame)

# Release everything when job is finished
out.release()
cv2.destroyAllWindows()

# Define paths for external audio and subtitle files
audio_filename = './tmp/sample_audio.mp3'
subtitle_filename = './tmp/sample_subtitles.srt'

# Intermediate filenames
video_with_audio_filename = video_filename.replace('.mp4', '_with_audio.mp4')
final_video_filename = video_filename.replace('.mp4', '_final.mp4')

# Add audio to the video
subprocess.call([
    'ffmpeg',
    '-i', video_filename,
    '-i', audio_filename,
    '-c:v', 'copy',
    '-c:a', 'aac',
    '-strict', 'experimental',
    video_with_audio_filename
])

# Apply fade-in and fade-out effects
subprocess.call([
    'ffmpeg',
    '-i', video_with_audio_filename,
    '-vf', 'fade=t=in:st=0:d=2,fade=t=out:st=3:d=1',
    '-c:a', 'copy',
    final_video_filename
])

# Embed subtitles into the video
subprocess.call([
    'ffmpeg',
    '-i', final_video_filename,
    '-vf', 'subtitles=' + subtitle_filename,
    '-c:a', 'copy',
    final_video_filename.replace('.mp4', '_with_subtitles.mp4')
])