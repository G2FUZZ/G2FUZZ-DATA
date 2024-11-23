import os
from mutagen.id3 import ID3, TIT2, TPE1, TALB, TCON, COMM, TXXX

# Create a directory to store the generated mp3 files
os.makedirs('./tmp/', exist_ok=True)

# Generate and save a sample mp3 file with extended ID3 tags
audio_file = './tmp/sample_extended_complex.mp3'
audio = ID3()
audio.add(TIT2(encoding=3, text="Sample Title"))
audio.add(TPE1(encoding=3, text="Sample Artist"))
audio.add(TALB(encoding=3, text="Sample Album"))
audio.add(TCON(encoding=3, text=["Genre1", "Genre2", "Genre3"]))  # Multiple genres
audio.add(COMM(encoding=3, lang='eng', desc='Comment', text='Sample Comment'))  # Comment
audio.add(TXXX(encoding=3, desc="CustomTag", text="Custom Value"))  # Custom user-defined tag
audio.save(audio_file)

print(f"Generated mp3 file with extended ID3 tags including multiple genres, comments, and custom tags: {audio_file}")