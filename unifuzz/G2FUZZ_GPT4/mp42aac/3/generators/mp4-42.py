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
video_filename = './tmp/complex_video.mp4'
encrypted_video_filename = './tmp/complex_video_encrypted.mp4'

# Create VideoWriter object
out = cv2.VideoWriter(video_filename, codec, fps, (width, height))

# Generate more complex video content
num_frames = 240  # 10 seconds of video at 24 fps
for i in range(num_frames):
    # Dynamic background color
    bg_color = (i % 255, (i*2) % 255, (i*3) % 255)
    frame = np.zeros((height, width, 3), np.uint8)  # Initial black background
    frame[:] = bg_color  # Set dynamic background color
    
    # Multiple moving shapes
    # Moving white square
    cv2.rectangle(frame, (10 + i, 50), (60 + i, 100), (255, 255, 255), -1)
    
    # Moving red circle
    cv2.circle(frame, (width - (10 + i*2), 100), 30, (0, 0, 255), -1)
    
    # Moving blue ellipse
    cv2.ellipse(frame, (320, 240), (100 + i % 50, 50 + i % 25), 0, 0, 180, (255, 0, 0), -1)
    
    # Adding text overlays
    text = f"Frame {i}"
    cv2.putText(frame, text, (50, height - 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
    
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