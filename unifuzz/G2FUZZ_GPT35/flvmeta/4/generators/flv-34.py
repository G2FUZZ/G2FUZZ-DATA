import os

# Create a directory to save the generated files
os.makedirs('./tmp/', exist_ok=True)

# Generate a more complex FLV file with multiple tags
flv_file_path = './tmp/complex.flv'
with open(flv_file_path, 'wb') as f:
    # Write FLV header
    f.write(b'FLV\x01\x01\x00\x00\x00\x09\x00\x00\x00\x00')
    
    # Write FLV tag 1 - Video Tag
    f.write(b'\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x00')  # Video Tag

    # Write FLV tag 2 - Audio Tag
    f.write(b'\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x00')  # Audio Tag

    # Write FLV tag 3 - Script Data Tag
    f.write(b'\x00\x00\x00\x00\x12\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x00')  # Script Data Tag

print(f'Complex FLV file generated at: {flv_file_path}')