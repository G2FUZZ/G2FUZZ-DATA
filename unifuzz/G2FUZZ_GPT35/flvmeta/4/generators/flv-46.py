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
        video_bitrate = random.randint(1000, 5000)  # Random video bitrate between 1000 to 5000 kbps
        frame_rate = random.choice([24, 30, 60])  # Random frame rate

        file_info = f'Video Duration: {video_duration} seconds | Video Resolution: {video_resolution} | Audio Codec: {audio_codec} | Video Bitrate: {video_bitrate} kbps | Frame Rate: {frame_rate}'
        f.write(file_info.encode())