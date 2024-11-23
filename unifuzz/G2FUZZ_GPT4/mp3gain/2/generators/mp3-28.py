from gtts import gTTS
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# The text to be converted to speech, now including the additional feature
text = """
7. Compatibility: MP3 is widely supported across almost all digital audio playing devices and software, making it one of the most universally compatible audio formats.
8. Backward Compatibility with MPEG-1: MP3 files encoded according to the MPEG-2 standard (which includes additional bit rates and sample rates not defined in MPEG-1) are designed to be backward compatible with MPEG-1 decoders, ensuring a wide base of compatibility with existing software and hardware.
"""

# Convert the text to speech
tts = gTTS(text=text, lang='en')

# Save the generated MP3 file
mp3_filename = './tmp/features.mp3'
tts.save(mp3_filename)

print(f"MP3 file has been saved to {mp3_filename}")