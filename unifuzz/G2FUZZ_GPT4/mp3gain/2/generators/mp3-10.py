from gtts import gTTS
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Text to be converted into speech
text = "MP3 files are suitable for streaming over the internet due to their small size and ability to be decoded in real-time, which has made them popular for online music services."

# Convert text to speech
tts = gTTS(text, lang='en')

# Save the converted file
tts.save("./tmp/streaming_support.mp3")

print("MP3 file has been generated and saved to ./tmp/streaming_support.mp3")