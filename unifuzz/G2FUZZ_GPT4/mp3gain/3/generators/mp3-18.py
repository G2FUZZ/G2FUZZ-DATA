from gtts import gTTS
import os

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# The text to be converted to speech with the additional feature
text = """
7. **Portability and Compatibility**: MP3 files are widely supported across almost all digital audio devices and software, making them highly portable and compatible.
1. **Psychoacoustic Models**: MP3 uses psychoacoustic models to determine which parts of the audio to discard during compression. This model is based on the human hearing perception, focusing on masking effects where certain sounds become inaudible in the presence of louder sounds.
8. **Layer III Encoding**: MP3, also known as MPEG-1 Audio Layer III, utilizes a complex layer of compression that balances between reducing file size and maintaining audio fidelity, incorporating Huffman coding for more efficient data representation.
"""

# Creating a gTTS object
tts = gTTS(text=text, lang='en')

# Saving the audio file
audio_file_path = './tmp/extended_features.mp3'
tts.save(audio_file_path)

print(f"MP3 file saved at: {audio_file_path}")