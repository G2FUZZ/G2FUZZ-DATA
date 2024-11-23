from gtts import gTTS
import os

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# The text to be converted to speech with the existing and additional features
text = """
7. **Portability and Compatibility**: MP3 files are widely supported across almost all digital audio devices and software, making them highly portable and compatible.
1. **Psychoacoustic Models**: MP3 uses psychoacoustic models to determine which parts of the audio to discard during compression. This model is based on the human hearing perception, focusing on masking effects where certain sounds become inaudible in the presence of louder sounds.
7. **Spectral Band Replication (SBR)**: Though not a native feature of the original MP3 format, some advanced audio codecs that build on MP3 technology use SBR to enhance audio quality by replicating higher frequency bands from lower frequencies.
"""

# Creating a gTTS object
tts = gTTS(text=text, lang='en')

# Saving the audio file
audio_file_path = './tmp/extended_features.mp3'
tts.save(audio_file_path)

print(f"MP3 file saved at: {audio_file_path}")