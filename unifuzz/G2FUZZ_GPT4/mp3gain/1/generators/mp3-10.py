from gtts import gTTS
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Text to convert to speech
text = "Encoding and Decoding Efficiency: MP3 uses sophisticated encoding algorithms that efficiently compress audio data, and it can be decoded with relatively low computational power. This makes MP3 a practical format for use in various devices, including those with limited processing capabilities."

# Generate speech
tts = gTTS(text, lang='en')
mp3_path = './tmp/encoding_and_decoding_efficiency.mp3'
tts.save(mp3_path)

print(f"MP3 file has been generated and saved to {mp3_path}")