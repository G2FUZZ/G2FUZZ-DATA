import os
from mutagen import File
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import HeaderNotFoundError

# Create a directory to store the generated mp3 files
os.makedirs('./tmp/', exist_ok=True)

# Function to read MP3 file with error handling for HeaderNotFoundError
def read_mp3_file(file_path):
    try:
        audio = File(file_path)
        if audio.mime[0] == 'audio/mpeg':
            return audio
        else:
            raise HeaderNotFoundError("Not an MP3 file")
    except (HeaderNotFoundError, IndexError):
        print(f"HeaderNotFoundError: The file {file_path} is not a valid MP3 file.")
        return None

# Generate and save a sample mp3 file with Custom Bit Rate (CBR)
with open('./tmp/sample_custom_cbr.mp3', 'wb') as f:
    f.write(b'Generated MP3 file with Custom Bit Rate (CBR)')
    audio = read_mp3_file('./tmp/sample_custom_cbr.mp3')
    if audio:
        audio.add_tags(EasyID3)
        audio['title'] = 'Custom CBR Title'
        audio['artist'] = 'Custom CBR Artist'
        audio['album'] = 'Custom CBR Album'
        audio.save()

# Generate and save a sample mp3 file with Stereo mode
with open('./tmp/sample_stereo.mp3', 'wb') as f:
    f.write(b'Generated MP3 file with Stereo mode')
    audio = read_mp3_file('./tmp/sample_stereo.mp3')
    if audio:
        audio.add_tags(EasyID3)
        audio['title'] = 'Stereo Title'
        audio['artist'] = 'Stereo Artist'
        audio['album'] = 'Stereo Album'
        audio.save()

# Generate and save a sample mp3 file with Variable Bit Rate (VBR)
with open('./tmp/sample_vbr_advanced.mp3', 'wb') as f:
    f.write(b'Generated MP3 file with Advanced Variable Bit Rate (VBR)')
    audio = read_mp3_file('./tmp/sample_vbr_advanced.mp3')
    if audio:
        audio.add_tags(EasyID3)
        audio['title'] = 'VBR Advanced Title'
        audio['artist'] = 'VBR Advanced Artist'
        audio['album'] = 'VBR Advanced Album'
        audio.save()