import os
from mutagen.id3 import ID3, TIT2, TPE1, TALB

# Create a directory if it doesn't exist
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Generate a sample mp3 file with ID3 tags
file_path = './tmp/sample.mp3'
audio = ID3()
audio.add(TIT2(encoding=3, text="Sample Title"))
audio.add(TPE1(encoding=3, text="Sample Artist"))
audio.add(TALB(encoding=3, text="Sample Album"))
audio.save(file_path)

print(f"Generated mp3 file with ID3 tags at: {file_path}")