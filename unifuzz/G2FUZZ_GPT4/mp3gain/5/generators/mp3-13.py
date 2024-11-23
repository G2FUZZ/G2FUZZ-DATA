from gtts import gTTS
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# The text to be converted to speech, now including the new feature description
text = """Portability and Support: MP3's widespread acceptance ensures that it is supported by virtually all digital audio players, software media players, and smartphones, making it one of the most portable and supported audio file formats. 

**Error Checking and Resilience**: MP3 files include error checking and resilience features that allow for some degree of error correction or concealment, helping ensure consistent playback quality even if the file becomes slightly corrupted."""

# Convert the text to speech
tts = gTTS(text=text, lang='en')

# Save the generated speech to an MP3 file
tts.save('./tmp/portability_and_support_with_error_checking_and_resilience.mp3')