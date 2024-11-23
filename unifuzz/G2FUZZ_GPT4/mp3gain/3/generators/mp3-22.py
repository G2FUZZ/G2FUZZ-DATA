from gtts import gTTS
import os

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# The text to be converted to speech, now including Backward Compatibility
text = """
2. **Backward Compatibility**: MP3s are designed to be backward compatible, meaning that newer versions of MP3 encoders and decoders strive to maintain playback capability with files created using older versions.

7. **Portability and Compatibility**: MP3 files are widely supported across almost all digital audio devices and software, making them highly portable and compatible.
"""

# Creating a gTTS object
tts = gTTS(text=text, lang='en')

# Saving the audio file
audio_file_path = './tmp/features.mp3'
tts.save(audio_file_path)

print(f"MP3 file saved at: {audio_file_path}")