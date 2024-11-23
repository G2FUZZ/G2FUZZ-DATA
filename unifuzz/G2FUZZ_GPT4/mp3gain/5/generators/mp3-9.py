from gtts import gTTS
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# The text to be converted to speech
text = """Portability and Support: MP3's widespread acceptance ensures that it is supported by virtually all digital audio players, software media players, and smartphones, making it one of the most portable and supported audio file formats."""

# Convert the text to speech
tts = gTTS(text=text, lang='en')

# Save the generated speech to an MP3 file
tts.save('./tmp/portability_and_support.mp3')