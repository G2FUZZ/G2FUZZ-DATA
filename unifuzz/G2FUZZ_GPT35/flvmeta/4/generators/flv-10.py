import os

# Create a directory to save the generated FLV files
os.makedirs('./tmp/', exist_ok=True)

# Generate FLV files with subtitles and captions
for i in range(3):
    with open(f'./tmp/video_{i}.flv', 'wb') as f:
        f.write(b'FLV header')
        f.write(b'Subtitles and captions: This is an example subtitle for video ' + str(i).encode())