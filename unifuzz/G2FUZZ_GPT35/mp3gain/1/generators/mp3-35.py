import os
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2, TPE1, TALB, TCOM, TCON, TDRC, TRCK, COMM

# Create a directory to store the generated mp3 files
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample mp3 file with extended ID3 tags and comments
mp3_file_path = './tmp/sample_complex_extended.mp3'

audio = MP3()

# Add ID3 tags to the audio file
audio.tags = ID3()
audio.tags.add(TIT2(encoding=3, text='Sample Title'))
audio.tags.add(TPE1(encoding=3, text='Sample Artist'))
audio.tags.add(TALB(encoding=3, text='Sample Album'))
audio.tags.add(TCOM(encoding=3, text='Sample Composer'))
audio.tags.add(TCON(encoding=3, text='Sample Genre'))
audio.tags.add(TDRC(encoding=3, text='2022'))
audio.tags.add(TRCK(encoding=3, text='1/10'))

# Add a comment to the mp3 file
comment = COMM(encoding=3, lang='eng', desc='Sample Comment', text='This is a sample comment added to the mp3 file.')
audio.tags.add(comment)

# Save the audio tags to the file path
audio.save(mp3_file_path, v1=2, v2_version=3)

print("MP3 file with extended complex file structure (ID3 tags and comments) generated successfully.")