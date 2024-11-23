import cv2
import numpy as np
import os
from moviepy.editor import AudioFileClip, VideoFileClip, concatenate_audioclips
from scipy.io.wavfile import write  # Import the write function from scipy

# Ensure tmp directory exists
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Video settings
width, height = 640, 480
fps = 24
codec = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for .mp4 files
video_filename = './tmp/sample_video_low_latency.mp4'
audio_filename = './tmp/sample_audio.wav'  # Placeholder for audio filename
final_output_filename = './tmp/final_output_with_audio.mp4'

# Audio settings
sample_rate = 44100  # Sample rate in Hz
duration = 5  # Duration in seconds (should match video duration for better synchronization)
frequency = 440  # Frequency of the sine wave in Hz

# Generate audio data
t = np.linspace(0, duration, int(sample_rate * duration), False)  # Time axis
audio_data = np.sin(2 * np.pi * frequency * t)  # Generate sine wave
audio_data = (audio_data * 32767).astype(np.int16)  # Convert to 16-bit data

# Write the audio file
write(audio_filename, sample_rate, audio_data)

# Additional settings for low latency streaming
parameters = [
    (cv2.VIDEOWRITER_PROP_QUALITY, 95),
]

# Create VideoWriter object with additional parameters
out = cv2.VideoWriter(video_filename, codec, fps, (width, height))
for param, value in parameters:
    out.set(param, value)

# Generate video content
num_frames = 120
for i in range(num_frames):
    frame = np.zeros((height, width, 3), np.uint8)
    cv2.rectangle(frame, (10 + i*5, 50), (60 + i*5, 100), (255, 255, 255), -1)
    out.write(frame)

# Release everything when job is finished
out.release()

# Combine the video file with the audio file
video_clip = VideoFileClip(video_filename)
audio_clip = AudioFileClip(audio_filename)
final_clip = video_clip.set_audio(audio_clip)
final_clip.write_videofile(final_output_filename, codec='libx264', audio_codec='aac')

cv2.destroyAllWindows()