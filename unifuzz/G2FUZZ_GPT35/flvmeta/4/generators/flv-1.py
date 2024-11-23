import os

# Create a directory to save the generated files
os.makedirs('./tmp/', exist_ok=True)

# Generate a simple FLV file
flv_file_path = './tmp/test.flv'
with open(flv_file_path, 'wb') as f:
    # Write FLV header
    f.write(b'FLV\x01\x01\x00\x00\x00\x09\x00\x00\x00\x00')
    # Write FLV tag
    f.write(b'\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x00')

print(f'FLV file generated at: {flv_file_path}')