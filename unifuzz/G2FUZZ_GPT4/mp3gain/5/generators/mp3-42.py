from gtts import gTTS
import os

# Function to ensure the category directory exists
def ensure_category_dir_exists(category):
    category_path = os.path.join('./tmp/', category)
    os.makedirs(category_path, exist_ok=True)
    return category_path

# Splitting the text into sections for each category
sections = {
    "Portability and Support": """Portability and Support: MP3's widespread acceptance ensures that it is supported by virtually all digital audio players, software media players, and smartphones, making it one of the most portable and supported audio file formats.""",
    "Error Checking and Resilience": """Error Checking and Resilience: MP3 files include error checking and resilience features that allow for some degree of error correction or concealment, helping ensure consistent playback quality even if the file becomes slightly corrupted."""
}

# Process each section and save it in its corresponding category directory
for category, text in sections.items():
    # Ensure the category directory exists
    category_path = ensure_category_dir_exists(category)

    # Convert the section text to speech
    tts = gTTS(text=text, lang='en')

    # Define the filename based on the category
    filename = f"{category.lower().replace(' ', '_')}.mp3"
    file_path = os.path.join(category_path, filename)

    # Save the generated speech to an MP3 file in the category directory
    tts.save(file_path)

    print(f"Generated MP3 file saved at: {file_path}")