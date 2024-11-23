import os
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, TIT2, TPE1, TALB, TCON, TYER
from gtts import gTTS

# Ensure the 'os' module is imported at the beginning of your script
# This is crucial for file and directory operations, such as checking if a file exists

# Create the /tmp directory if it doesn't exist
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Generate a simple speech using gTTS and save as MP3
text_to_speech = "This is a test MP3 file with ID3 tags, including title, artist, album, and more."
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

# Adding album art (example: using a placeholder image from the web or a local file)
# Here you should have a valid image file. For this example, let's ensure there's a file named 'album_art.jpg' in the ./tmp/ directory.
image_path = './tmp/album_art.jpg'
if os.path.exists(image_path):
    with open(image_path, 'rb') as albumart:
        audio.tags.add(APIC(encoding=3, mime='image/jpeg', type=3, desc=u'Cover', data=albumart.read()))
else:
    print(f"Warning: The file {image_path} does not exist. Skipping album art addition.")

audio.save()

print(f"MP3 file with ID3 tags created at: {mp3_file_path}")