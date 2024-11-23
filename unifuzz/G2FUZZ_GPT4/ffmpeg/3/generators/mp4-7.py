from moviepy.editor import ColorClip
from cryptography.fernet import Fernet
import os

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Step 1: Generate a simple video clip
clip = ColorClip(size=(640, 480), color=(255, 0, 0), duration=5)
clip.write_videofile('./tmp/original_video.mp4', fps=24)

# Step 2: Encrypt the video
# Generate a key for encryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Read the video file
with open('./tmp/original_video.mp4', 'rb') as file:
    original_video_data = file.read()

# Encrypt the data
encrypted_data = cipher_suite.encrypt(original_video_data)

# Save the encrypted data to a new file
with open('./tmp/encrypted_video.mp4', 'wb') as encrypted_file:
    encrypted_file.write(encrypted_data)

# Note: To decrypt the video, you would use the `decrypt` method of the cipher_suite object 
# and the same key. This is a demonstration of a concept and is not suitable for real DRM applications.