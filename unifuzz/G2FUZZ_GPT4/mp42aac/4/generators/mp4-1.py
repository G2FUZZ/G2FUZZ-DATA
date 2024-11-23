import cv2
import numpy as np
import wave
import struct
import os
from moviepy.editor import VideoFileClip, AudioFileClip, CompositeVideoClip

# Ensure the tmp directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Video settings
width, height = 640, 480
fps = 24
duration = 5  # seconds
background_color = (255, 255, 255)
text_color = (0, 0, 255)
font = cv2.FONT_HERSHEY_SIMPLEX

# Audio settings
frequency = 440  # Hz, sine wave frequency of A4
sample_rate = 44100  # Samples per second
audio_duration = duration  # seconds

# Generate video frames
video_filename = os.path.join(output_dir, 'output_video.mp4')
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter(video_filename, fourcc, fps, (width, height))

for i in range(fps * duration):
    img = np.full((height, width, 3), background_color, np.uint8)
    cv2.putText(img, "Hello, World!", (50, height // 2 + int(i / 2) % (height - 50)), font, 1, text_color, 2)
    video.write(img)
video.release()

# Generate audio
audio_filename = os.path.join(output_dir, 'output_audio.wav')
audio = wave.open(audio_filename, 'w')
audio.setparams((1, 2, sample_rate, 0, 'NONE', 'not compressed'))

values = []
for i in range(int(sample_rate * audio_duration)):
    value = int(32767.0*np.cos(frequency*2.0*np.pi*float(i)/float(sample_rate)))
    packed_value = struct.pack('h', value)
    values.append(packed_value)

value_str = b''.join(values)
audio.writeframes(value_str)
audio.close()

# Combine the video and audio
video_clip = VideoFileClip(video_filename)
audio_clip = AudioFileClip(audio_filename)
final_clip = video_clip.set_audio(audio_clip)
final_filename = os.path.join(output_dir, 'final_output.mp4')
final_clip.write_videofile(final_filename, codec='libx264', audio_codec='aac')

# Clean up temporary files
os.remove(video_filename)
os.remove(audio_filename)