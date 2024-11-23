import os

# Create a directory to store the generated FLV files
os.makedirs('./tmp/', exist_ok=True)

# Generate FLV files with more complex file structures
for i in range(3):
    filename = f'./tmp/video_{i}.flv'
    with open(filename, 'wb') as file:
        if i == 0:
            # First FLV file with metadata and video frames
            metadata = b'Metadata: { "title": "Sample Video", "author": "John Doe", "duration": "10s" }'
            file.write(metadata)
            for frame in range(5):
                file.write(f'Video Frame {frame}'.encode())
        elif i == 1:
            # Second FLV file with audio data and video frames
            audio_data = b'Audio Data: { "format": "mp3", "bitrate": "128kbps" }'
            file.write(audio_data)
            for frame in range(3):
                file.write(f'Video Frame {frame}'.encode())
        else:
            # Third FLV file with different video codec and frame rate
            video_codec = b'Video Codec: H.264'
            frame_rate = b'Frame Rate: 30fps'
            file.write(video_codec)
            file.write(frame_rate)
            for frame in range(7):
                file.write(f'Video Frame {frame}'.encode())

print('FLV files with more complex file structures have been generated and saved in ./tmp/ directory.')