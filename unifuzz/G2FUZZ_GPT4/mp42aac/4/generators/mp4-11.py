import numpy as np
import cv2
import wave
import contextlib
import os  # Ensure os is imported
from moviepy.editor import *

# Create a temporary directory if it doesn't exist
tmp_dir = './tmp/'
os.makedirs(tmp_dir, exist_ok=True)

# Generate a simple animation with OpenCV
frame_count = 300
frame_width = 640
frame_height = 480
fps = 30

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_path = os.path.join(tmp_dir, 'lossless_compression_video.mp4')
out = cv2.VideoWriter(video_path, fourcc, fps, (frame_width, frame_height))

for i in range(frame_count):
    # Create a frame with a moving circle
    frame = np.zeros((frame_height, frame_width, 3), np.uint8)
    cv2.circle(frame, (frame_width // 2 + int(frame_width * 0.3 * np.sin(2 * np.pi * i / frame_count)),
                       frame_height // 2 + int(frame_height * 0.3 * np.cos(2 * np.pi * i / frame_count))),
               50, (0, 255, 0), -1)
    out.write(frame)

# Release everything
out.release()

# Generate a lossless WAV file
sample_rate = 44100  # Sample rate in Hz
duration = frame_count / fps  # seconds

t = np.linspace(0., duration, int(sample_rate * duration))
audio_data = (np.sin(2 * np.pi * 440 * t) * 32767).astype(np.int16)

wav_path = os.path.join(tmp_dir, 'lossless_audio.wav')
with wave.open(wav_path, 'w') as wav:
    wav.setnchannels(1)  # mono
    wav.setsampwidth(2)  # two bytes per sample
    wav.setframerate(sample_rate)
    wav.writeframes(audio_data.tobytes())

# Combine the video and audio using MoviePy
video_clip = VideoFileClip(video_path)
audio_clip = AudioFileClip(wav_path)
final_clip = video_clip.set_audio(audio_clip)
final_clip.write_videofile(os.path.join(tmp_dir, 'final_lossless_video.mp4'), codec='libx264', audio_codec='aac')