import os

# Create a directory for storing the generated FLV files
os.makedirs('./tmp/', exist_ok=True)

# Generate FLV files with multiple audio tracks and custom metadata
for i in range(4):
    file_name = f'./tmp/video_{i+1}.flv'
    with open(file_name, 'wb') as file:
        if i == 0:
            file.write(b'FLV Streaming Support: Online Video Playback\nAudio Tracks: English, Spanish\nMetadata: {"title": "Sample Video 1", "author": "John Doe"}')
        elif i == 1:
            file.write(b'FLV Streaming Support: Online Video Playback\nAudio Tracks: English, French, German\nMetadata: {"title": "Sample Video 2", "author": "Jane Smith"}')
        elif i == 2:
            file.write(b'FLV Streaming Support: Online Video Playback\nAudio Tracks: Japanese, Korean\nMetadata: {"title": "Sample Video 3", "author": "Alice"}')
        else:
            file.write(b'FLV Streaming Support: Online Video Playback\nAudio Tracks: Arabic\nMetadata: {"title": "Sample Video 4", "author": "Bob"}')

    print(f'FLV file "{file_name}" with multiple audio tracks and custom metadata has been generated.')