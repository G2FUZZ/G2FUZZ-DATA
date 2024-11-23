from gtts import gTTS
import os

# Define the text you want to convert to audio
text = """
9. **Portability and Compatibility**: MP3 files are highly portable and compatible with virtually all digital audio players, smartphones, and computers. This universal compatibility, along with their small file size, has made MP3 one of the most popular audio formats worldwide.
"""

# Specify the language of the text
language = 'en'

# Create a gTTS object
tts = gTTS(text=text, lang=language, slow=False)

# Specify the directory to save the MP3 file
save_directory = './tmp/'
os.makedirs(save_directory, exist_ok=True)

# Define the filename
filename = 'text_to_speech.mp3'

# Save the converted audio to a file
tts.save(os.path.join(save_directory, filename))

print(f"MP3 file has been saved to {os.path.join(save_directory, filename)}")