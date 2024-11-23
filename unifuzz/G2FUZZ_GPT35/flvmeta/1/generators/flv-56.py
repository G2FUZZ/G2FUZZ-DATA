import os

def generate_flv_file(filename, metadata, video_data, audio_data):
    header = b'FLV\x01\x05\x00\x00\x00\x09\x00\x00\x00\x00'
    previous_tag_size = b'\x00\x00\x00\x00'
    
    with open(filename, 'wb') as file:
        file.write(header)
        
        # Write metadata tag
        metadata_tag = create_tag(b'\x12', metadata)
        file.write(metadata_tag)
        
        # Write video data tag
        video_tag = create_tag(b'\x09', video_data)
        file.write(video_tag)
        
        # Write audio data tag
        audio_tag = create_tag(b'\x08', audio_data)
        file.write(audio_tag)
        
        file.write(previous_tag_size)

def create_tag(tag_type, data):
    tag_data_size = len(data).to_bytes(3, byteorder='big')
    timestamp = b'\x00\x00\x00\x00\x00'
    stream_id = b'\x00\x00\x00'
    tag = tag_type + tag_data_size + timestamp + stream_id + data
    tag_size = len(tag).to_bytes(4, byteorder='big')
    return tag_size + tag

# Create a directory to store the generated FLV files
os.makedirs('./tmp/', exist_ok=True)

# Generate FLV files with additional metadata, video, and audio data
metadata = b'Metadata: { "title": "Sample Video", "author": "John Doe", "duration": "00:01:30" }'
video_data = b'\x00\x00\x00\x00\x00'  # Example video data
audio_data = b'\x01\x01\x01\x01\x01'  # Example audio data

for i in range(5):
    filename = f'./tmp/video_{i}.flv'
    generate_flv_file(filename, metadata, video_data, audio_data)

print('FLV files with additional metadata, video, and audio data have been generated and saved in ./tmp/ directory.')