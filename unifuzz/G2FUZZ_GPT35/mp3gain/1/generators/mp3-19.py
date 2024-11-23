import os
from mutagen.id3 import ID3, TIT2, TPE1, TALB, TXXX

# Create a directory if it doesn't exist
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Generate a sample mp3 file with ID3 tags and custom tag
file_path = './tmp/sample_custom.mp3'
audio_custom = ID3()
audio_custom.add(TIT2(encoding=3, text="Sample Title"))
audio_custom.add(TPE1(encoding=3, text="Sample Artist"))
audio_custom.add(TALB(encoding=3, text="Sample Album"))
audio_custom.add(TXXX(encoding=3, desc="Custom Description", text="Custom Value"))
audio_custom.save(file_path)

print(f"Generated mp3 file with ID3 tags and Custom tag at: {file_path}")