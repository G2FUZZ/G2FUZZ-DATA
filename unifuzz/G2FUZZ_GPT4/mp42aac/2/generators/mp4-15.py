from moviepy.editor import ColorClip
from mutagen.mp4 import MP4, MP4Cover, MP4Tags
import os
from cryptography.fernet import Fernet

# Ensure the tmp directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create a simple video clip (for example, a 5-second red screen)
clip = ColorClip(size=(640, 480), color=(255, 0, 0), duration=5)
video_path = os.path.join(output_dir, 'example_video.mp4')
clip.write_videofile(video_path, fps=24)

# Now let's add metadata to our MP4 file
video = MP4(video_path)

# Adding metadata
video["\xa9nam"] = "Example Title"  # Title
video["\xa9ART"] = "Artist Name"  # Artist
video["\xa9alb"] = "Album Name"  # Album
video["\xa9day"] = "2023"  # Year
video["\xa9cmt"] = "A sample video with metadata"  # Comment

# Save the file with metadata
video.save()

# Sample Encryption
# Generate a key for encryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Encrypt the video file
with open(video_path, 'rb') as original_file:
    original_data = original_file.read()

encrypted_data = cipher_suite.encrypt(original_data)

# Write the encrypted data to a new file
encrypted_video_path = os.path.join(output_dir, 'example_video_encrypted.mp4')
with open(encrypted_video_path, 'wb') as encrypted_file:
    encrypted_file.write(encrypted_data)

# Saving the encryption key to a file (for decryption purposes)
key_path = os.path.join(output_dir, 'encryption_key.key')
with open(key_path, 'wb') as key_file:
    key_file.write(key)

print(f"Encrypted video saved to {encrypted_video_path}")
print(f"Encryption key saved to {key_path}")