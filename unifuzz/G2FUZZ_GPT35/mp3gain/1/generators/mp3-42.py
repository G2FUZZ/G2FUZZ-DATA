import os
from mutagen.id3 import ID3, TIT2, TPE1, TALB, APIC, USLT, TCON

# Create a directory if it doesn't exist
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Generate a sample mp3 file with extended ID3 tags
file_path = './tmp/sample_extended.mp3'
audio = ID3()

# Title and Artist information
audio.add(TIT2(encoding=3, text="Sample Title"))
audio.add(TPE1(encoding=3, text="Sample Artist"))

# Album and Genre information
audio.add(TALB(encoding=3, text="Sample Album"))
audio.add(TCON(encoding=3, text="Pop"))

# Attached picture (album art)
with open('album_art.jpg', 'rb') as img_file:
    album_art = img_file.read()
audio.add(APIC(3, 'image/jpeg', 3, 'Front cover', album_art))

# Lyrics
lyrics = "Sample lyrics for the song."
audio.add(USLT(encoding=3, lang='eng', desc='Lyrics', text=lyrics))

audio.save(file_path)

print(f"Generated mp3 file with extended ID3 tags at: {file_path}")