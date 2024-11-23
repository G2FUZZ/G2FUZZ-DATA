import os

# Create a directory to save the generated files
os.makedirs('./tmp/', exist_ok=True)

# Generate a more complex FLV file with multiple audio/video tracks, subtitles, and metadata
flv_file_path = './tmp/complex_flv_file.flv'
with open(flv_file_path, 'wb') as f:
    # Write FLV header
    f.write(b'FLV\x01\x05\x00\x00\x00\x09\x00\x00\x00\x00')
    # Write FLV tag with Video data
    f.write(b'\x00\x00\x00\x13\x09\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00')
    # Write FLV tag with Audio data
    f.write(b'\x00\x00\x00\x13\x08\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00')
    # Write FLV tag with Subtitles
    f.write(b'\x00\x00\x00\x13\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x00\x00\x00\x00\x00\x00')
    # Write FLV tag with Metadata
    f.write(b'\x00\x00\x00\x13\x12\x00\x00\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00')

print(f'More complex FLV file generated at: {flv_file_path}')