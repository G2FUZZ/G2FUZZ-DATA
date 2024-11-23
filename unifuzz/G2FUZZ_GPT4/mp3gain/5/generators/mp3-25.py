from gtts import gTTS
import os

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Text to be converted into speech, now including Customizable Quality Settings
text = """
8. **Backward Compatibility**: MP3 files are designed to be backward compatible with older players. This means that despite the improvements and changes in encoding techniques over the years, MP3 files can still be played by a wide range of audio playback devices.

4. **Customizable Quality Settings**: During encoding, users can often customize quality settings beyond just the bit rate, such as selecting the algorithm quality level, which balances between file size and the encoding time against the perceived audio quality.
"""

# Creating a gTTS object
tts = gTTS(text=text, lang='en')

# Saving the converted audio in a MP3 file
mp3_file = './tmp/features.mp3'
tts.save(mp3_file)

print(f"MP3 file has been saved at {mp3_file}")