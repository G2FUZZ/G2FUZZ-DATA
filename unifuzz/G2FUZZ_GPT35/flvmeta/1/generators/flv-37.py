import os

# Create a directory to save generated FLV files
os.makedirs('./tmp/', exist_ok=True)

# Generate FLV files with multiple video tracks, audio tracks, metadata, and script data
for i in range(3):
    file_name = f'./tmp/complex_video_{i}.flv'
    with open(file_name, 'wb') as f:
        # Generate FLV content with multiple video tracks, audio tracks, metadata, and script data
        flv_content = b'FLV_HEADER'

        # Add video track
        video_track = f'Video {i} content'.encode('utf-8')
        flv_content += b'\x01' + len(video_track).to_bytes(3, byteorder='big') + video_track

        # Add audio track
        audio_track = f'Audio {i} content'.encode('utf-8')
        flv_content += b'\x02' + len(audio_track).to_bytes(3, byteorder='big') + audio_track

        # Add metadata
        metadata = b'Metadata content'
        flv_content += b'\x12' + len(metadata).to_bytes(3, byteorder='big') + metadata

        # Add script data
        script_data = b'Script data content'
        flv_content += b'\x18' + len(script_data).to_bytes(3, byteorder='big') + script_data

        # Add timestamp for each track
        video_timestamp = i * 1000  # Sample video timestamp calculation
        audio_timestamp = i * 2000  # Sample audio timestamp calculation
        metadata_timestamp = i * 3000  # Sample metadata timestamp calculation
        script_data_timestamp = i * 4000  # Sample script data timestamp calculation
        flv_content += b'\x03' + video_timestamp.to_bytes(4, byteorder='big')
        flv_content += b'\x04' + audio_timestamp.to_bytes(4, byteorder='big')
        flv_content += b'\x05' + metadata_timestamp.to_bytes(4, byteorder='big')
        flv_content += b'\x06' + script_data_timestamp.to_bytes(4, byteorder='big')

        f.write(flv_content)

print('FLV files with more complex file structures generated successfully!')