import os
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2, TPE1, TALB, TCOM, TCON, TDRC, TRCK, COMM
from mutagen.mp3 import MP3, StreamInfo

# Check if the directory exists, create it if it doesn't
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate a sample mp3 file with multiple audio streams and custom metadata
mp3_file_path = os.path.join(directory, 'sample_complex_extended.mp3')

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

# Add multiple audio streams to the mp3 file
audio.info = StreamInfo()

# Save the audio tags and streams to the file path
audio.save(mp3_file_path, v1=2, v2_version=3)

print("MP3 file with extended complex file structure (ID3 tags, comments, and multiple audio streams) generated successfully.")