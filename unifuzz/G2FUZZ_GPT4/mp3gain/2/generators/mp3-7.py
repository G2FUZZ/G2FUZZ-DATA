from gtts import gTTS
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# The text to be converted to speech
text = "7. Compatibility: MP3 is widely supported across almost all digital audio playing devices and software, making it one of the most universally compatible audio formats."

# Convert the text to speech
tts = gTTS(text=text, lang='en')

# Save the generated MP3 file
mp3_filename = './tmp/compatibility.mp3'
tts.save(mp3_filename)

print(f"MP3 file has been saved to {mp3_filename}")