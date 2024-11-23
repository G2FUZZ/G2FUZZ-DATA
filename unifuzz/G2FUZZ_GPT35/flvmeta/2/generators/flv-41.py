import os
import random

# Create a directory to store the generated FLV files if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate FLV files with varying durations and resolutions
video_info = [
    {'duration': 10, 'resolution': '720p'},  # 720p resolution and 10 seconds duration
    {'duration': 15, 'resolution': '1080p'},  # 1080p resolution and 15 seconds duration
    {'duration': 8, 'resolution': '480p'},  # 480p resolution and 8 seconds duration
    {'duration': 12, 'resolution': '720p'},  # 720p resolution and 12 seconds duration
    {'duration': 20, 'resolution': '1080p'}  # 1080p resolution and 20 seconds duration
]

for idx, video in enumerate(video_info):
    duration = video['duration']  # in seconds
    resolution = video['resolution']

    # Generate dummy video data based on duration and resolution
    if resolution == '720p':
        file_size = random.randint(500, 800)  # Random file size between 500 KB and 800 KB for 720p
    elif resolution == '1080p':
        file_size = random.randint(800, 1200)  # Random file size between 800 KB and 1200 KB for 1080p
    else:
        file_size = random.randint(300, 500)  # Random file size between 300 KB and 500 KB for other resolutions

    with open(f'./tmp/video_{idx}_{resolution}_{duration}s.flv', 'wb') as f:
        # Write dummy data to create a file with the specified size
        f.write(b'\0' * file_size * 1024)

print("FLV files with varying durations and resolutions have been generated and saved in the './tmp/' directory.")