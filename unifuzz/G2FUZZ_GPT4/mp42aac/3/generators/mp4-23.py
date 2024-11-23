import cv2
import numpy as np
import os
from cryptography.fernet import Fernet

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
video_filename = './tmp/sample_video.mp4'
encrypted_video_filename = './tmp/sample_video_encrypted.mp4'

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

# Encrypting video file
with open(video_filename, 'rb') as file:
    file_data = file.read()
    encrypted_data = encrypt(file_data, key)

# Writing encrypted video file
with open(encrypted_video_filename, 'wb') as file:
    file.write(encrypted_data)

# Note: Decryption would be needed to view the video