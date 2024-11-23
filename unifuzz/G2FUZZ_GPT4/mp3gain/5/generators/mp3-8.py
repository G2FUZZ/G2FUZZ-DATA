from gtts import gTTS
import os

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Text to be converted into speech
text = """
8. **Backward Compatibility**: MP3 files are designed to be backward compatible with older players. This means that despite the improvements and changes in encoding techniques over the years, MP3 files can still be played by a wide range of audio playback devices.
"""

# Creating a gTTS object
tts = gTTS(text=text, lang='en')

# Saving the converted audio in a MP3 file
mp3_file = './tmp/backward_compatibility.mp3'
tts.save(mp3_file)

print(f"MP3 file has been saved at {mp3_file}")