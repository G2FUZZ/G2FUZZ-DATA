import os

def generate_complex_flv_file():
    # Create a directory to store the generated FLV files
    os.makedirs('./tmp/', exist_ok=True)

    # Generate FLV file with complex features
    filename = './tmp/complex_flv_file.flv'
    with open(filename, 'wb') as f:
        # FLV header
        f.write(b'FLV\x01\x05\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00\x00')

        # Audio tag with AAC codec
        f.write(b'\x08\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        f.write(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')

        # Audio tag with MP3 codec
        f.write(b'\x08\x01\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        f.write(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')

        # Video tag with H.264 codec
        f.write(b'\x09\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        f.write(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')

        # Video tag with VP8 codec
        f.write(b'\x09\x01\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        f.write(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')

        print(f'FLV file with complex features generated: {filename}')

# Generate a FLV file with complex features
generate_complex_flv_file()