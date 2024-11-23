from gtts import gTTS
import os
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Base directory for saving MP3 files
base_dir = './tmp/'

# Ensure the base directory exists
os.makedirs(base_dir, exist_ok=True)

# Categories for the MP3 files
categories = ['Portability_Compatibility', 'Psychoacoustic_Models', 'Spectral_Band_Replication']

texts = {
    'Portability_Compatibility': """
        7. **Portability and Compatibility**: MP3 files are widely supported across almost all digital audio devices and software, making them highly portable and compatible.
    """,
    'Psychoacoustic_Models': """
        1. **Psychoacoustic Models**: MP3 uses psychoacoustic models to determine which parts of the audio to discard during compression. This model is based on the human hearing perception, focusing on masking effects where certain sounds become inauditable in the presence of louder sounds.
    """,
    'Spectral_Band_Replication': """
        7. **Spectral Band Replication (SBR)**: Though not a native feature of the original MP3 format, some advanced audio codecs that build on MP3 technology use SBR to enhance audio quality by replicating higher frequency bands from lower frequencies.
    """
}

def generate_mp3(category, text):
    # Create category-specific directory if it doesn't exist
    category_path = os.path.join(base_dir, category)
    os.makedirs(category_path, exist_ok=True)

    # File name with current timestamp
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    file_name = f"{category}_{timestamp}.mp3"
    file_path = os.path.join(category_path, file_name)

    # Creating a gTTS object
    tts = gTTS(text=text.strip(), lang='en')

    # Saving the audio file
    tts.save(file_path)

    logging.info(f"MP3 file saved at: {file_path}")

# Generate MP3 files for each category
for category, text in texts.items():
    generate_mp3(category, text)