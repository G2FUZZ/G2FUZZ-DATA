import os

# Create a directory to store the generated FLV files
os.makedirs('./tmp/', exist_ok=True)

# Generate FLV file with streaming support feature
filename = './tmp/streaming_support.flv'
with open(filename, 'wb') as f:
    # FLV header
    f.write(b'FLV\x01\x01\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00\x00')
    
    # FLV body with streaming support feature
    f.write(b'\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x00')
    f.write(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
    
print(f'FLV file with streaming support feature generated: {filename}')