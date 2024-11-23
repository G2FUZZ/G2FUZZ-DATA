import os
from mutagen.id3 import ID3, TIT2, TPE1, TALB, TXXX

# Create a directory if it doesn't exist
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Generate a sample mp3 file with ID3 tags, custom tag, and Encryption feature
file_path = './tmp/sample_encrypted.mp3'
audio_encrypted = ID3()
audio_encrypted.add(TIT2(encoding=3, text="Sample Title"))
audio_encrypted.add(TPE1(encoding=3, text="Sample Artist"))
audio_encrypted.add(TALB(encoding=3, text="Sample Album"))
audio_encrypted.add(TXXX(encoding=3, desc="Custom Description", text="Custom Value"))
audio_encrypted.add(TXXX(encoding=3, desc="Encryption", text="Encrypted content"))
audio_encrypted.save(file_path)

print(f"Generated mp3 file with ID3 tags, Custom tag, and Encryption feature at: {file_path}")