import os

def generate_complex_flv_file(file_path):
    with open(file_path, 'wb') as f:
        # Write FLV header
        f.write(b'FLV\x01\x01\x00\x00\x00\x09\x00\x00\x00\x00')
        
        # Write FLV tag 1 - Video Tag
        f.write(b'\x00\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x00')  # Video Tag
        
        # Write FLV tag 2 - Audio Tag
        f.write(b'\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x00')  # Audio Tag
        
        # Write FLV tag 3 - Script Data Tag
        f.write(b'\x00\x00\x00\x00\x12\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x00')  # Script Data Tag
        
        # Write additional custom tags or data structures here
        # Example:
        # Custom Tag 1
        f.write(b'\x00\x00\x00\x00\x0F\x00\x00\x00\x00\x00\x00\x00\x0A\x00\x00\x00\x00')  # Custom Tag 1
        
        # Custom Tag 2
        f.write(b'\x00\x00\x00\x00\x0E\x00\x00\x00\x00\x00\x00\x00\x0A\x00\x00\x00\x00')  # Custom Tag 2

    return file_path

# Create a directory to save the generated files
os.makedirs('./tmp/', exist_ok=True)

# Generate a more complex FLV file with additional tags and data structures
flv_file_path = './tmp/complex_extended.flv'
flv_file_path = generate_complex_flv_file(flv_file_path)

print(f'Complex extended FLV file generated at: {flv_file_path}')