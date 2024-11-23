import os

def generate_flv_file(file_path, audio_data, video_data, metadata):
    with open(file_path, 'wb') as f:
        # FLV header
        f.write(b'\x46\x4c\x56\x01\x01\x00\x00\x00\x09\x00\x00\x00\x00')
        
        # PreviousTagSize0 (placeholder for first tag size)
        f.write(b'\x00\x00\x00\x00')
        
        # Audio Data
        f.write(b'\x08')  # Audio tag
        f.write(len(audio_data).to_bytes(3, byteorder='big'))  # Data size
        f.write(b'\x00\x00\x00')  # Timestamp
        f.write(audio_data)
        f.write(len(audio_data).to_bytes(4, byteorder='big'))  # Tag size
        
        # Video Data
        f.write(b'\x09')  # Video tag
        f.write(len(video_data).to_bytes(3, byteorder='big'))  # Data size
        f.write(b'\x00\x00\x00')  # Timestamp
        f.write(video_data)
        f.write(len(video_data).to_bytes(4, byteorder='big'))  # Tag size
        
        # Metadata
        metadata_size = len(metadata)
        f.write(b'\x18')  # Metadata tag
        f.write(metadata_size.to_bytes(3, byteorder='big'))  # Data size
        f.write(b'\x00\x00\x00')  # Timestamp
        f.write(metadata.encode())
        f.write((metadata_size + 11).to_bytes(4, byteorder='big'))  # Tag size

# Create a directory to store the generated FLV files if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate a more complex FLV file
audio_data = b'Audio data here'
video_data = b'Video data here'
metadata = 'Custom metadata: { "title": "Sample Video", "duration": "10s" }'

generate_flv_file('./tmp/complex_video.flv', audio_data, video_data, metadata)

print("A more complex FLV file has been generated and saved as 'complex_video.flv' in the './tmp/' directory.")