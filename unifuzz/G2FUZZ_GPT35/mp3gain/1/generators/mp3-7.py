import os

# Create a directory to save the generated mp3 files
os.makedirs('./tmp/', exist_ok=True)

# Generate an example mp3 file with streaming capability feature
with open('./tmp/streaming_capability.mp3', 'wb') as file:
    file.write(b'Example MP3 file with streaming capability feature')

print('MP3 file with streaming capability feature generated and saved in ./tmp/')