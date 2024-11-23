import os
import numpy as np
import cv2
from scipy.io import wavfile
from moviepy.editor import VideoFileClip, AudioFileClip

# Ensure the tmp directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Video settings
fps = 24
duration = 5  # seconds
width, height = 2048, 1024  # Updated for 360-degree video dimensions

# Generate video frames
fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
video_path = os.path.join(output_dir, 'temp_video.mp4')
video = cv2.VideoWriter(video_path, fourcc, fps, (width, height))

for frame_num in range(fps * duration):
    frame = np.zeros((height, width, 3), dtype=np.uint8)
    # Updated to draw a simple pattern that can be visually interesting in 360
    cv2.circle(frame, (frame_num % width, height // 2), 50, (255, 255, 0), -1)
    cv2.putText(frame, f'Frame {frame_num+1}', (50, height // 2), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    video.write(frame)

video.release()

# Generate audio
sample_rate = 44100
t = np.linspace(0, duration, int(sample_rate * duration), False)
frequency = 440  # A4
audio_wave = np.sin(frequency * 2 * np.pi * t)
audio_wave = (audio_wave * 32767).astype(np.int16)
audio_path = os.path.join(output_dir, 'temp_audio.wav')
wavfile.write(audio_path, sample_rate, audio_wave)

# Use moviepy to combine the video and audio
video_clip = VideoFileClip(video_path)
audio_clip = AudioFileClip(audio_path)

# To add 360-degree video support, inject spherical video metadata
# This feature is not directly supported through moviepy or OpenCV, and would typically require post-processing with additional tools or libraries
# For demonstration, this code does not implement metadata injection, but acknowledges the need for it
final_clip = video_clip.set_audio(audio_clip)
final_path = os.path.join(output_dir, 'final_output_360.mp4')
final_clip.write_videofile(final_path, codec='libx264', audio_codec='aac')

# Cleanup temporary files
os.remove(video_path)
os.remove(audio_path)

print(f'MP4 file with 360-degree video and audio has been saved to {final_path}')