import cv2
import numpy as np
import os
from moviepy.editor import VideoFileClip, AudioFileClip

# Ensure the tmp directory exists
os.makedirs('./tmp', exist_ok=True)

# Video parameters
width, height = 640, 480
fps = 24
duration = 5  # seconds
output_video_path = './tmp/generated_video.mp4'

# Generate video frames
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

for frame_num in range(fps * duration):
    # Create a frame with changing colors
    color = tuple(np.random.randint(0, 255, size=3).tolist())
    frame = np.full((height, width, 3), color, dtype=np.uint8)
    video.write(frame)

video.release()

# Generate synthetic audio
from scipy.io.wavfile import write
import numpy as np

audio_output_path = './tmp/generated_audio.wav'
samplerate = 44100
t = np.linspace(0., duration, samplerate * duration)
frequency = 440  # A4
audio = 0.5 * np.sin(2. * np.pi * frequency * t)

write(audio_output_path, samplerate, audio.astype(np.float32))

# Combine video and audio
video_clip = VideoFileClip(output_video_path)
audio_clip = AudioFileClip(audio_output_path)
final_clip = video_clip.set_audio(audio_clip)
final_clip.write_videofile('./tmp/final_output.mp4', codec='libx264', audio_codec='aac')

# Clean up temporary files
os.remove(output_video_path)
os.remove(audio_output_path)