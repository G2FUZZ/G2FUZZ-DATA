import os
import random

# Define the audio and video codecs
audio_codecs = ['AAC', 'MP3', 'Nellymoser']
video_codecs = ['H.264', 'VP8', 'MPEG-4']
timestamps = ['00:00:05', '00:01:30', '00:03:15']

# Create the directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate FLV files with random audio, video codecs, and timestamps
for i in range(5):
    file_name = f'./tmp/file_{i}.flv'
    audio_codec = random.choice(audio_codecs)
    video_codec = random.choice(video_codecs)
    timestamp = random.choice(timestamps)
    
    with open(file_name, 'wb') as file:
        file.write(f'Audio Codec: {audio_codec}\nVideo Codec: {video_codec}\nTimestamp: {timestamp}'.encode())
    
    print(f'Generated FLV file: {file_name}')