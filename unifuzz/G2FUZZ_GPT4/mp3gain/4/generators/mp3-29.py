import os
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, TIT2, TPE1, TALB, TCON, TYER, TSSE
from gtts import gTTS
from pydub import AudioSegment

# Ensure the 'os' module is imported at the beginning of your script

# Create the /tmp directory if it doesn't exist
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Generate a simple speech using gTTS and save as MP3
text_to_speech = "This is a test MP3 file with ID3 tags, including title, artist, album, and more, plus encoder-specific optimizations."
tts = gTTS(text_to_speech, lang='en')
mp3_file_path = './tmp/test_mp3_file.mp3'
tts.save(mp3_file_path)

# Define ID3 tags
audio = MP3(mp3_file_path, ID3=ID3)

# Add ID3 tag if it doesn't exist
try:
    audio.add_tags()
except Exception as e:
    print(e)

# Details for ID3 tags
audio.tags.add(TIT2(encoding=3, text='Test Title'))
audio.tags.add(TPE1(encoding=3, text='Test Artist'))
audio.tags.add(TALB(encoding=3, text='Test Album'))
audio.tags.add(TCON(encoding=3, text='Podcast'))
audio.tags.add(TYER(encoding=3, text='2023'))

# Adding Encoder-Specific Optimizations tag
audio.tags.add(TSSE(encoding=3, text="LAME 3.99r"))

# Adding album art
image_path = './tmp/album_art.jpg'
if os.path.exists(image_path):
    with open(image_path, 'rb') as albumart:
        audio.tags.add(APIC(encoding=3, mime='image/jpeg', type=3, desc=u'Cover', data=albumart.read()))
else:
    print(f"Warning: The file {image_path} does not exist. Skipping album art addition.")

audio.save()

# Seamless Looping Feature
# Load the original MP3 file
original_audio = AudioSegment.from_mp3(mp3_file_path)

# Assuming we want to make a 30-second loop for simplicity
loop_duration = 30 * 1000  # 30 seconds in milliseconds
loop_audio = original_audio[:loop_duration]
# Ensure the loop is exactly 30 seconds
loop_audio = loop_audio * (loop_duration // len(loop_audio)) + loop_audio[:loop_duration % len(loop_audio)]

# Fade in and fade out to make the loop seamless
fade_duration = 2000  # 2 seconds in milliseconds
loop_audio = loop_audio.fade_in(fade_duration).fade_out(fade_duration)

# Save the looped file
looped_mp3_file_path = './tmp/test_mp3_file_looped.mp3'
loop_audio.export(looped_mp3_file_path, format="mp3")

print(f"MP3 file with ID3 tags, Seamless Looping, and Encoder-Specific Optimizations created at: {looped_mp3_file_path}")