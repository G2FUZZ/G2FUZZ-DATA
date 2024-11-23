import os
import random

# Create a directory to store the generated FLV files
os.makedirs('./tmp/', exist_ok=True)

# Generate FLV files with additional complex features
for i in range(1, 4):
    with open(f'./tmp/file_{i}.flv', 'wb') as f:
        video_duration = random.randint(60, 600)  # Random video duration between 1 to 10 minutes
        video_resolution = f'1920x1080'  # Video resolution
        audio_codec = 'AAC'  # Audio codec

        file_info = f'Video Duration: {video_duration} seconds | Video Resolution: {video_resolution} | Audio Codec: {audio_codec}'
        f.write(file_info.encode())