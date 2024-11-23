import os

# Create a directory to save the generated files
os.makedirs('./tmp/', exist_ok=True)

# Generate a FLV file with Interactive menus feature
flv_file_path = './tmp/test_with_interactive_menus.flv'
with open(flv_file_path, 'wb') as f:
    # Write FLV header
    f.write(b'FLV\x01\x01\x00\x00\x00\x09\x00\x00\x00\x00')
    # Write FLV tag with Interactive menus
    f.write(b'\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x00\x07\x00\x00\x00\x00')

print(f'FLV file with Interactive menus generated at: {flv_file_path}')