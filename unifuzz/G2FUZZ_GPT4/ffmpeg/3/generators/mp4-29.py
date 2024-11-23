from moviepy.editor import ColorClip, concatenate_audioclips
from moviepy.audio.AudioClip import AudioArrayClip
from cryptography.fernet import Fernet
import os
import numpy as np

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate a simple video clip
clip = ColorClip(size=(640, 480), color=(255, 0, 0), duration=5)

# Generate a silent audio clip instead of loading from a file
# Here, we create 5 seconds of silence with a sample rate of 44100 Hz
sample_rate = 44100
duration = 5  # seconds
silent_audio = np.zeros((sample_rate * duration, 2))  # 2 channels for stereo
audio_clip = AudioArrayClip(silent_audio, fps=sample_rate)

# Extend or manipulate the audio clip as needed for priming
audio_clip = concatenate_audioclips([audio_clip, audio_clip])

# Set the audio of the video clip
clip = clip.set_audio(audio_clip)

# Write the video file with audio
clip.write_videofile('./tmp/original_video_with_audio.mp4', fps=24)

# Encrypt the video
# Generate a key for encryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Read the video file
with open('./tmp/original_video_with_audio.mp4', 'rb') as file:
    original_video_data = file.read()

# Encrypt the data
encrypted_data = cipher_suite.encrypt(original_video_data)

# Save the encrypted data to a new file
with open('./tmp/encrypted_video_with_audio.mp4', 'wb') as encrypted_file:
    encrypted_file.write(encrypted_data)

# Note: To decrypt the video, you would use the `decrypt` method of the cipher_suite object 
# and the same key. This is a demonstration of a concept and is not suitable for real DRM applications.