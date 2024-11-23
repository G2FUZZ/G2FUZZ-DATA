import os

# Create a directory to save the generated MP3 files
os.makedirs('./tmp/', exist_ok=True)

# Generate a dummy MP3 file with streaming support feature
with open('./tmp/streaming_support.mp3', 'w') as file:
    file.write('Streaming support: MP3 files can be streamed over the internet for online playback.')