import os

def generate_flv_file(filename, metadata):
    header = b'FLV\x01\x05\x00\x00\x00\x09\x00\x00\x00\x00'
    previous_tag_size = b'\x00\x00\x00\x00'
    
    with open(filename, 'wb') as file:
        file.write(header)
        
        # Write metadata tag
        tag_type = b'\x12'  # Metadata tag type
        tag_data_size = len(metadata).to_bytes(3, byteorder='big')
        timestamp = b'\x00\x00\x00\x00\x00'
        stream_id = b'\x00\x00\x00'
        tag = tag_type + tag_data_size + timestamp + stream_id + metadata
        tag_size = len(tag).to_bytes(4, byteorder='big')
        
        file.write(tag_size + tag + previous_tag_size)

# Create a directory to store the generated FLV files
os.makedirs('./tmp/', exist_ok=True)

# Generate FLV files with additional metadata information
metadata = b'Metadata: { "title": "Sample Video", "author": "John Doe", "duration": "00:01:30" }'
for i in range(5):
    filename = f'./tmp/video_{i}.flv'
    generate_flv_file(filename, metadata)

print('FLV files with additional metadata have been generated and saved in ./tmp/ directory.')