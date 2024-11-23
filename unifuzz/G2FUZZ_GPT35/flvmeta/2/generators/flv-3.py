import os

# Define the metadata for the FLV file
metadata = {
    'duration': 120,
    'width': 1920,
    'height': 1080,
    'frame_rate': 30
}

# Create the FLV file
file_path = './tmp/test.flv'
with open(file_path, 'wb') as f:
    # Write metadata to the file
    f.write(b'FLV\x01\x05\x00\x00\x00\x09\x00\x00\x00\x00')
    f.write(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
    f.write(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
    f.write(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
    f.write(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
    f.write(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
    f.write(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
    f.write(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')