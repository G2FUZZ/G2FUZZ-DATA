import os

# Create a directory to save generated FLV files
os.makedirs('./tmp/', exist_ok=True)

# Generate FLV files with multiple video tracks, audio tracks, and timestamps
for i in range(3):
    file_name = f'./tmp/video_{i}.flv'
    with open(file_name, 'wb') as f:
        # Generate FLV content with multiple video tracks, audio tracks, and timestamps
        flv_content = b'FLV_HEADER'

        # Add video track
        video_track = f'Video {i} content'.encode('utf-8')
        flv_content += b'\x01' + len(video_track).to_bytes(3, byteorder='big') + video_track

        # Add audio track
        audio_track = f'Audio {i} content'.encode('utf-8')
        flv_content += b'\x02' + len(audio_track).to_bytes(3, byteorder='big') + audio_track

        # Add timestamp for each track
        timestamp = i * 1000  # Sample timestamp calculation
        flv_content += b'\x03' + timestamp.to_bytes(4, byteorder='big')

        f.write(flv_content)

print('FLV files with multiple video tracks, audio tracks, and timestamps generated successfully!')