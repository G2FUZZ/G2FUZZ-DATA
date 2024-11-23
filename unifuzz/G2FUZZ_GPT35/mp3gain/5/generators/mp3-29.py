import os
from mutagen.id3 import ID3, TIT2, TPE1, TALB, TCON, TXXX, APIC

# Create a directory to store the generated mp3 files
os.makedirs('./tmp/', exist_ok=True)

# Generate and save a sample mp3 file with more complex file structures
audio_file = './tmp/sample_complex.mp3'
audio = ID3()
audio.add(TIT2(encoding=3, text="Sample Title"))
audio.add(TPE1(encoding=3, text="Sample Artist"))
audio.add(TALB(encoding=3, text="Sample Album"))
audio.add(TCON(encoding=3, text="Sample Genre"))
audio.add(TXXX(encoding=3, desc="Custom Data", text="Additional information"))

# Create a sample 'album_art.jpg' file
with open('album_art.jpg', 'wb') as f:
    f.write(b'Sample album art content')

# Add the sample image (album art) to the mp3 file
with open('album_art.jpg', 'rb') as album_art:
    audio.add(APIC(
        encoding=3,
        mime='image/jpeg',
        type=3,
        desc='Cover',
        data=album_art.read()
    ))

audio.save(audio_file)

print(f"Generated mp3 file with more complex file structures: {audio_file}")