from gtts import gTTS
import os
from datetime import datetime

# Function to ensure the directory structure exists
def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

# Current date to organize the files by date
current_date = datetime.now().strftime("%Y-%m-%d")

# Base directory where files will be saved
base_dir = './tmp/audio_files/'

# Example categories and subcategories
categories = {
    'education': ['mathematics', 'science', 'history'],
    'technology': ['software', 'hardware']
}

texts = {
    'mathematics': "Mathematics is an area of knowledge that involves the study of such topics as numbers, formulas, and related structures.",
    'science': "Science is a systematic enterprise that builds and organizes knowledge in the form of testable explanations and predictions about the universe.",
    'history': "History is the study of the past. Events before the invention of writing systems are considered prehistory.",
    'software': "Software is a collection of instructions that tell a computer how to work. This is in contrast to hardware, from which the system is built and actually performs the work.",
    'hardware': "Computer hardware includes the physical parts of a computer, such as the case, central processing unit (CPU), random access memory (RAM), monitor, mouse, keyboard, computer data storage, graphics card, sound card, speakers, and motherboard."
}

for category, subcategories in categories.items():
    for subcategory in subcategories:
        # Text for the TTS
        text = texts.get(subcategory, "No text provided.")
        
        # Creating a gTTS object
        tts = gTTS(text=text, lang='en')
        
        # Constructing the file path
        file_path = f"{base_dir}{category}/{subcategory}/{current_date}/{subcategory}.mp3"
        
        # Ensuring the directory exists
        ensure_dir(file_path)
        
        # Saving the audio file
        tts.save(file_path)
        
        print(f"MP3 file saved at: {file_path}")