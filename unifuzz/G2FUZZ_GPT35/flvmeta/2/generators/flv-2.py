import os
import random

# Define the audio codecs
audio_codecs = ['AAC', 'MP3', 'Nellymoser']

# Create the directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate FLV files with random audio codecs
for i in range(5):
    file_name = f'./tmp/file_{i}.flv'
    audio_codec = random.choice(audio_codecs)
    
    with open(file_name, 'wb') as file:
        file.write(f'Audio Codec: {audio_codec}'.encode())
    
    print(f'Generated FLV file: {file_name}')