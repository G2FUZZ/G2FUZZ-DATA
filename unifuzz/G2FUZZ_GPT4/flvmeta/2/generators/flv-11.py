import cv2
import numpy as np
from moviepy.editor import *
import os
from scipy.io import wavfile

# Ensure the tmp directory exists
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Generate a single blue frame
frame_height = 720
frame_width = 1280
color_blue = (255, 0, 0)
image = np.zeros((frame_height, frame_width, 3), np.uint8)
image[:] = color_blue

# Specify the output path and the codec
output_path = './tmp/output_video.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

# Create a VideoWriter object and write the frame
out = cv2.VideoWriter(output_path, fourcc, 1, (frame_width, frame_height))
out.write(image)
out.release()

# Generate a synthetic audio track (sine wave) for demonstration
duration = 1
sample_rate = 44100
t = np.linspace(0, duration, int(sample_rate * duration), False)
frequency = 440
audio = np.sin(2 * np.pi * frequency * t)
audio = (audio * 32767).astype(np.int16)

# Save the audio to a file
audio_path = './tmp/synthetic_audio.wav'
wavfile.write(audio_path, sample_rate, audio)

# Combine the video and the synthetic audio
video_clip = VideoFileClip(output_path)
audio_clip = AudioFileClip(audio_path)
final_clip = video_clip.set_audio(audio_clip)

# Convert the video to a more compatible format without specifying an unsupported audio codec
final_clip.write_videofile('./tmp/final_video.mp4', fps=24)