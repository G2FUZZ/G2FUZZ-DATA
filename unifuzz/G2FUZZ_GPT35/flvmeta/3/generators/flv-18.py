import os

# Create a directory to store the generated FLV files
os.makedirs('./tmp/', exist_ok=True)

# Generate FLV files with encryption and Chapter Navigation features
for i in range(4):
    file_name = f'./tmp/file_{i}.flv'
    with open(file_name, 'wb') as f:
        # Simulating encryption by writing some random data
        f.write(os.urandom(1024))
        # Adding Chapter Navigation feature by writing chapter markers
        chapter_markers = [b'Chapter 1: Introduction', b'Chapter 2: Main Content', b'Chapter 3: Conclusion']
        for marker in chapter_markers:
            f.write(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
            f.write(len(marker).to_bytes(2, byteorder='big'))
            f.write(marker)

print('FLV files with encryption and Chapter Navigation features have been generated and saved in ./tmp/ directory.')