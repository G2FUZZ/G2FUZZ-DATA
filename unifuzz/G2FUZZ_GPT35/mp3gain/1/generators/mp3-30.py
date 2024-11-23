import os
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, TIT2, TPE1, TALB, TCON
from PIL import Image

# Create a directory if it does not exist
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample mp3 file with complex metadata
sample_data = "Editable: MP3 files can be edited and manipulated using various software tools.\nDigital rights management (DRM): Some MP3 files may include DRM protection to restrict unauthorized copying or distribution."
file_path = './tmp/sample_complex_metadata.mp3'

audio = MP3()
audio.add_tags()

tags = ID3()

# Add metadata to the mp3 file
tags.add(TIT2(encoding=3, text="Sample Title"))
tags.add(TPE1(encoding=3, text="Sample Artist"))
tags.add(TALB(encoding=3, text="Sample Album"))
tags.add(TCON(encoding=3, text="Sample Genre"))

# Add album art to the mp3 file
image_path = './tmp/sample_album_art.jpg'
image = Image.new('RGB', (100, 100), color='red')
image.save(image_path)
with open(image_path, 'rb') as album_art:
    tags.add(APIC(3, 'image/jpeg', 3, 'Front cover', album_art.read()))

tags.save(file_path)

audio.save(file_path)

print(f"Generated mp3 file with complex metadata: {file_path}")