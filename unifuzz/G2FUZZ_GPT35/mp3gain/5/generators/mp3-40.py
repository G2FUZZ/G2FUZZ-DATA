import os
from mutagen.id3 import ID3, TIT2, TPE1, TALB, TCON, TXXX, APIC

# Create a directory to store the generated mp3 files
os.makedirs('./tmp/', exist_ok=True)

# Generate and save a sample mp3 file with even more complex file structures
audio_file = './tmp/sample_super_complex_extended.mp3'
audio = ID3()
audio.add(TIT2(encoding=3, text="Sample Title"))
audio.add(TPE1(encoding=3, text="Sample Artist"))
audio.add(TALB(encoding=3, text="Sample Album"))
audio.add(TCON(encoding=3, text="Sample Genre"))
audio.add(TXXX(encoding=3, desc="Custom Data 1", text="Additional information 1"))
audio.add(TXXX(encoding=3, desc="Custom Data 2", text="Additional information 2"))
audio.add(TXXX(encoding=3, desc="Custom Data 3", text="Additional information 3"))

# Create sample image files
image_files = ['album_art_1.jpg', 'album_art_2.jpg', 'album_art_3.jpg']

# Add multiple images to the mp3 file
for index, image_file in enumerate(image_files):
    with open(image_file, 'wb') as f:
        f.write(f'Sample album art content {index + 1}'.encode())

    with open(image_file, 'rb') as album_art:
        audio.add(APIC(
            encoding=3,
            mime='image/jpeg',
            type=3,
            desc=f'Cover {index + 1}',
            data=album_art.read()
        ))

# Add a longer description to the mp3 file
long_description = "This is a sample mp3 file with multiple custom tags, multiple images, and a longer description."
audio.add(TXXX(encoding=3, desc="Long Description", text=long_description))

audio.save(audio_file)

print(f"Generated mp3 file with even more complex file structures: {audio_file}")