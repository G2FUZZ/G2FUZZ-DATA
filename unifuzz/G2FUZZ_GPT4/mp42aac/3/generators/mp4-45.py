import cv2
import numpy as np
import os
from cryptography.fernet import Fernet
from moviepy.editor import VideoFileClip, AudioFileClip

# Function to encrypt data
def encrypt(data, key):
    fernet = Fernet(key)
    return fernet.encrypt(data)

# Function to decrypt data
def decrypt(data, key):
    fernet = Fernet(key)
    return fernet.decrypt(data)

# Generate a key for encryption
key = Fernet.generate_key()

# Ensure tmp directory exists
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Video settings
width, height = 640, 480
fps = 24
codec = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for .mp4 files
video_filename = './tmp/complex_video.mp4'
encrypted_video_filename = './tmp/complex_video_encrypted.mp4'
decrypted_video_filename = './tmp/complex_video_decrypted.mp4'
audio_filename = './tmp/background_music.mp3'

# Create VideoWriter object
out = cv2.VideoWriter(video_filename, codec, fps, (width, height))

# Generate more complex video content
num_frames = 240  # 10 seconds of video at 24 fps
for i in range(num_frames):
    # Dynamic background color
    bg_color = (i % 255, (i*2) % 255, (i*3) % 255)
    frame = np.zeros((height, width, 3), np.uint8)
    frame[:] = bg_color
    
    # Add shapes, text, etc. here
    
    out.write(frame)

# Release everything when job is finished
out.release()
cv2.destroyAllWindows()

# Check if the audio file exists before proceeding
if os.path.exists(audio_filename):
    # Add background music to the video
    video_clip = VideoFileClip(video_filename)
    audio_clip = AudioFileClip(audio_filename)
    final_clip = video_clip.set_audio(audio_clip)
    final_clip.write_videofile(encrypted_video_filename, codec='libx264', audio_codec='aac')
else:
    print(f"Audio file {audio_filename} not found, proceeding without adding background music.")

# Encryption/Decryption steps here