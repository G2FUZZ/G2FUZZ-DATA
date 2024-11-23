import os
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2, TPE1, TALB

# Create a directory to store the generated mp3 files
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample mp3 file with ID3 tags
# You can use the Mutagen library to add ID3 tags to the mp3 file
mp3_file_path = './tmp/sample_complex.mp3'

audio = MP3()
audio.add_tags()
audio.tags.add(TIT2(encoding=3, text='Sample Title'))
audio.tags.add(TPE1(encoding=3, text='Sample Artist'))
audio.tags.add(TALB(encoding=3, text='Sample Album'))

# Save the audio tags directly to the file path
audio.save(mp3_file_path)

print("MP3 file with complex file structure (ID3 tags) generated successfully.")