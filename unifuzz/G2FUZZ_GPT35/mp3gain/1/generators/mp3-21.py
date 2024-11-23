import os
from mutagen.id3 import ID3, TIT2, TPE1, TALB, TXXX, COMM

# Create a directory if it doesn't exist
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Generate a sample mp3 file with ID3 tags and custom tag
file_path = './tmp/sample_surround_sound.mp3'
audio_surround = ID3()
audio_surround.add(TIT2(encoding=3, text="Sample Title"))
audio_surround.add(TPE1(encoding=3, text="Sample Artist"))
audio_surround.add(TALB(encoding=3, text="Sample Album"))
audio_surround.add(TXXX(encoding=3, desc="Custom Description", text="Custom Value"))
audio_surround.add(COMM(encoding=3, lang='eng', desc='Surround sound encoding', text='Dolby Digital for multi-channel audio'))
audio_surround.save(file_path)

print(f"Generated mp3 file with ID3 tags, Custom tag, and Surround sound encoding at: {file_path}")