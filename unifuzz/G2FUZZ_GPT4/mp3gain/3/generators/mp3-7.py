from gtts import gTTS
import os

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)  # Corrected argument name here

# The text to be converted to speech
text = """
7. **Portability and Compatibility**: MP3 files are widely supported across almost all digital audio devices and software, making them highly portable and compatible.
"""

# Creating a gTTS object
tts = gTTS(text=text, lang='en')

# Saving the audio file
audio_file_path = './tmp/portability_and_compatibility.mp3'
tts.save(audio_file_path)

print(f"MP3 file saved at: {audio_file_path}")