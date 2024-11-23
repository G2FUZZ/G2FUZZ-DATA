import os
from mutagen.id3 import ID3, TIT2, TPE1, TALB, TCON, TXXX, APIC

# Create a directory to store the generated mp3 files
os.makedirs('./tmp/', exist_ok=True)

# Generate and save a sample mp3 file with even more complex file structures
audio_file = './tmp/sample_super_complex_extended.mp3'
audio = ID3()
audio.add(TIT2(encoding=3, text="Super Sample Title"))
audio.add(TPE1(encoding=3, text="Super Sample Artist"))
audio.add(TALB(encoding=3, text="Super Sample Album"))
audio.add(TCON(encoding=3, text="Super Sample Genre"))
audio.add(TXXX(encoding=3, desc="Custom Data 1", text="Super Additional information 1"))
audio.add(TXXX(encoding=3, desc="Custom Data 2", text="Super Additional information 2"))

# Create sample image files
image_files = ['super_album_art_1.jpg', 'super_album_art_2.jpg', 'super_album_art_3.jpg']

# Add multiple images to the mp3 file
for index, image_file in enumerate(image_files):
    with open(image_file, 'wb') as f:
        f.write(f'Super Sample album art content {index + 1}'.encode())

    with open(image_file, 'rb') as album_art:
        audio.add(APIC(
            encoding=3,
            mime='image/jpeg',
            type=3,
            desc=f'Super Cover {index + 1}',
            data=album_art.read()
        ))

# Add more complex file features like multiple text frames
audio.add(TXXX(encoding=3, desc="Custom Data 3", text="Super Additional information 3"))
audio.add(TXXX(encoding=3, desc="Custom Data 4", text="Super Additional information 4"))

audio.save(audio_file)

print(f"Generated mp3 file with even more complex file features: {audio_file}")