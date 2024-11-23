import os
from mutagen.id3 import ID3, TIT2, TPE1, TALB, TCON, COMM, TXXX

# Create a directory to store the generated mp3 files
os.makedirs('./tmp/', exist_ok=True)

# Generate and save a sample mp3 file with extended ID3 tags
audio_file = './tmp/sample_extended_complex_v2.mp3'
audio = ID3()
audio.add(TIT2(encoding=3, text="Sample Title"))
audio.add(TPE1(encoding=3, text=["Sample Artist 1", "Sample Artist 2"]))  # Multiple artists
audio.add(TALB(encoding=3, text="Sample Album"))
audio.add(TCON(encoding=3, text=["Genre1", "Genre2", "Genre3"]))  # Multiple genres
audio.add(COMM(encoding=3, lang='eng', desc='Comment 1', text='Sample Comment 1'))  # Comment 1
audio.add(COMM(encoding=3, lang='eng', desc='Comment 2', text='Sample Comment 2'))  # Comment 2
audio.add(TXXX(encoding=3, desc="CustomTag1", text="Custom Value 1"))  # Custom user-defined tag 1
audio.add(TXXX(encoding=3, desc="CustomTag2", text="Custom Value 2"))  # Custom user-defined tag 2
audio.save(audio_file)

print(f"Generated mp3 file with extended ID3 tags including multiple artists, genres, comments, and custom tags: {audio_file}")