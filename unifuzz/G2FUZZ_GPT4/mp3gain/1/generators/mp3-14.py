import os
from pydub import AudioSegment
from pydub.generators import Sine
from mutagen.id3 import ID3, TIT2, TPE1, TALB, TCON, TRCK, TYER, APIC, COMM
from mutagen.mp3 import MP3

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate a sine wave tone for 5 seconds, 440 Hz
tone = Sine(440).to_audio_segment(duration=5000)

# Save the generated tone to a file with adjustable quality settings
file_path = './tmp/generated_tone_with_quality.mp3'

# Quality settings
bit_rate = "192k"  # Higher bit rates provide better quality. Common rates: 128k, 192k, 320k
vbr = "5"  # VBR quality 0(highest) to 9(lowest). VBR is variable bit rate.
abr = False  # ABR is average bit rate. Set to True to use ABR, False otherwise.
cbr = False  # CBR is constant bit rate. Set to True to use CBR, False otherwise.

if abr:
    # ABR Mode
    tone.export(file_path, format="mp3", bitrate=bit_rate, parameters=["-abr", "1"])
elif cbr:
    # CBR Mode
    tone.export(file_path, format="mp3", bitrate=bit_rate)
else:
    # VBR Mode (default)
    tone.export(file_path, format="mp3", parameters=["-q:a", vbr])

# Add metadata to the mp3 file
audio = MP3(file_path, ID3=ID3)

# Add various metadata
audio.tags.add(TIT2(encoding=3, text='Generated Tone with Quality Settings'))
audio.tags.add(TPE1(encoding=3, text='Python Script'))
audio.tags.add(TALB(encoding=3, text='Generated Sounds'))
audio.tags.add(TCON(encoding=3, text='Synth'))
audio.tags.add(TRCK(encoding=3, text='1'))
audio.tags.add(TYER(encoding=3, text='2023'))

# Optional: Add an album cover
# with open('path/to/cover.jpg', 'rb') as albumart:
#     audio.tags.add(APIC(encoding=3, mime='image/jpeg', type=3, desc=u'Cover', data=albumart.read()))

# Optional: Add a comment
audio.tags.add(COMM(encoding=3, lang=u'eng', desc='desc', text='This is a generated MP3 file with adjustable quality settings'))

audio.save()

print(f"Generated MP3 with adjustable quality settings and metadata saved to {file_path}")