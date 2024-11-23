import os

# Create a directory to save the generated files
os.makedirs('./tmp/', exist_ok=True)

# Generate a FLV file with multiple tags, audio, video data, and metadata information
flv_file_path = './tmp/complex_flv_file.flv'
with open(flv_file_path, 'wb') as f:
    # Write FLV header
    f.write(b'FLV\x01\x01\x00\x00\x00\x09\x00\x00\x00\x00')
    
    # FLV tag with audio data
    f.write(b'\x08\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x00\x07\x00\x00\x00\x00')
    # Audio data (dummy data for example)
    f.write(b'\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00')
    
    # FLV tag with video data
    f.write(b'\x09\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x00\x07\x00\x00\x00\x00')
    # Video data (dummy data for example)
    f.write(b'\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00')
    
    # FLV tag with metadata information
    f.write(b'\x12\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x00\x07\x00\x00\x00\x00')
    # Metadata information (dummy data for example)
    f.write(b'\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00')

print(f'Complex FLV file generated at: {flv_file_path}')