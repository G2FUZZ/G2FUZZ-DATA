import eyed3
import os

# Create a directory to store the generated mp3 files
os.makedirs('./tmp/', exist_ok=True)

# Generate a complex mp3 file with multiple audio frames and custom ID3 tags
with open('./tmp/sample_complex.mp3', 'wb') as f:
    # First audio frame with a specific bit rate
    f.write(b'Audio Frame 1 with 128kbps')

    # Second audio frame with a different bit rate
    f.write(b'Audio Frame 2 with 256kbps')

# Load the generated complex mp3 file
audiofile_complex = eyed3.load('./tmp/sample_complex.mp3')

# Check if audiofile_complex is not None before accessing its tag attributes
if audiofile_complex is not None:
    audiofile_complex.tag.artist = 'Complex Artist'
    audiofile_complex.tag.album = 'Complex Album'
    audiofile_complex.tag.title = 'Complex Title'
    audiofile_complex.tag.track_num = 1
    # Custom ID3 tag
    audiofile_complex.tag.custom['Key'] = 'Value'
    audiofile_complex.tag.save()
    print('Generated complex mp3 file with multiple audio frames and custom ID3 tags successfully.')
else:
    print('Error: Failed to load the complex mp3 file.')