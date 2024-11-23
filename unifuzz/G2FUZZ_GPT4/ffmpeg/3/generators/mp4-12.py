from moviepy.editor import ColorClip, AudioFileClip, concatenate_audioclips
from cryptography.fernet import Fernet
import os
import json

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Step 1: Generate a simple video clip
clip = ColorClip(size=(640, 480), color=(255, 0, 0), duration=5)
clip.write_videofile('./tmp/original_video.mp4', fps=24)

# Step 2: Create or load multiple audio tracks
audio_files_exist = True
audio_file_paths = ['./tmp/audio_track_1.mp3', './tmp/audio_track_2.mp3']

# Check if audio files exist
for audio_file_path in audio_file_paths:
    if not os.path.exists(audio_file_path):
        print(f"Warning: The file {audio_file_path} could not be found!")
        audio_files_exist = False

if audio_files_exist:
    # Load the audio tracks
    audio_track_1 = AudioFileClip(audio_file_paths[0])
    audio_track_2 = AudioFileClip(audio_file_paths[1])

    # Concatenate audio tracks
    multi_audio = concatenate_audioclips([audio_track_1, audio_track_2])

    # Step 3: Add the multi-track audio to the video clip
    video_with_audio = clip.set_audio(multi_audio)

    # Step 4: Write the video file with multi-track audio
    video_with_audio.write_videofile('./tmp/video_with_multitrack_audio.mp4', fps=24)
else:
    # If audio files do not exist, proceed without adding audio
    clip.write_videofile('./tmp/video_with_multitrack_audio.mp4', fps=24)

# Sample Description generation
sample_description = {
    "format": "mp4",
    "video": {
        "resolution": "640x480",
        "color": "red",
        "fps": 24
    },
    "audio": {
        "tracks": 2 if audio_files_exist else 0,
        "format": "mp3" if audio_files_exist else "none"
    }
}

# Save the sample description to a JSON file
with open('./tmp/sample_description.json', 'w') as json_file:
    json.dump(sample_description, json_file, indent=4)

# Step 5: Encrypt the video with multi-track audio (if audio exists) or without audio
# Generate a key for encryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Read the video file
with open('./tmp/video_with_multitrack_audio.mp4', 'rb') as file:
    video_data = file.read()

# Encrypt the data
encrypted_data = cipher_suite.encrypt(video_data)

# Save the encrypted data to a new file
with open('./tmp/encrypted_video_with_multitrack_audio.mp4', 'wb') as encrypted_file:
    encrypted_file.write(encrypted_data)