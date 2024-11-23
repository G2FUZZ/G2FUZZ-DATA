import os

# Create a directory to save generated FLV files
os.makedirs('./tmp/', exist_ok=True)

# Generate FLV files with more complex file structures
for i in range(3):
    file_name = f'./tmp/complex_video_{i}.flv'
    with open(file_name, 'wb') as f:
        # Generate FLV content with more complex file structures
        flv_content = b'FLV_HEADER'

        # Add metadata
        metadata = b'Metadata: { "title": "Video Title", "author": "Author Name" }'
        flv_content += b'\x04' + len(metadata).to_bytes(4, byteorder='big') + metadata

        # Add keyframe
        keyframe = b'Keyframe: Sample Keyframe Data'
        flv_content += b'\x05' + len(keyframe).to_bytes(4, byteorder='big') + keyframe

        # Add additional video track
        additional_video_track = f'Additional Video {i} content'.encode('utf-8')
        flv_content += b'\x06' + len(additional_video_track).to_bytes(4, byteorder='big') + additional_video_track

        # Add additional audio track
        additional_audio_track = f'Additional Audio {i} content'.encode('utf-8')
        flv_content += b'\x07' + len(additional_audio_track).to_bytes(4, byteorder='big') + additional_audio_track

        # Add timestamps for each track
        video_timestamp = i * 1000  # Sample video timestamp calculation
        audio_timestamp = i * 500  # Sample audio timestamp calculation
        flv_content += b'\x08' + video_timestamp.to_bytes(4, byteorder='big')
        flv_content += b'\x09' + audio_timestamp.to_bytes(4, byteorder='big')

        f.write(flv_content)

print('FLV files with more complex file structures generated successfully!')