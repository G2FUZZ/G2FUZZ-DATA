from gtts import gTTS
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# The text to be converted to speech, including the new feature description
text = """
7. Compatibility: MP3 is widely supported across almost all digital audio playing devices and software, making it one of the most universally compatible audio formats.
5. MPEG-2 and MPEG-2.5 Extensions: Besides the standard MPEG-1 Audio Layer III (MP3) format, extensions like MPEG-2 Layer III offer lower bit rate options suitable for lower quality applications, and MPEG-2.5 Layer III extends MP3 to support very low sampling rates for applications like speech.
"""

# Convert the text to speech
tts = gTTS(text=text, lang='en')

# Save the generated MP3 file
mp3_filename = './tmp/compatibility_extensions.mp3'
tts.save(mp3_filename)

print(f"MP3 file has been saved to {mp3_filename}")