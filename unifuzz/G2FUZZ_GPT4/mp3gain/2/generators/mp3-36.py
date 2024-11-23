from gtts import gTTS
import os
from mutagen.id3 import ID3, APIC, TIT2, TPE1, TALB, TRCK, TYER
from mutagen.mp3 import MP3

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Texts to be converted into speech, simulating chapters of an audiobook
texts = [
    "Chapter 1: In the beginning, MP3 files revolutionized the way we consume music...",
    "Chapter 2: The technology behind MP3 encoding involves complex psychoacoustic models...",
    # Add more chapters as needed
]

# Metadata for the audiobook
audiobook_title = "The History of MP3"
audiobook_author = "Jane Doe"
audiobook_album = "Understanding Digital Audio"
year = "2023"

# Specify the path to your cover image here
cover_image_path = 'cover.png'

for i, text in enumerate(texts, start=1):
    chapter_title = f"Chapter {i}"
    
    # Convert text to speech
    tts = gTTS(text, lang='en')
    mp3_filename = f"./tmp/{audiobook_title}_Chapter_{i}.mp3"
    tts.save(mp3_filename)
    
    # Load the saved MP3 file to add metadata
    audio = MP3(mp3_filename, ID3=ID3)
    
    # Check if the file has ID3 tag, if not, create a new one
    if audio.tags is None:
        audio.add_tags()
    
    # Add cover image if it exists
    if os.path.exists(cover_image_path):
        with open(cover_image_path, 'rb') as img_file:
            audio.tags.add(APIC(mime='image/png', type=3, desc='Cover', data=img_file.read()))
    else:
        print(f"Warning: Cover image file '{cover_image_path}' not found. Skipping cover image addition.")

    # Add other ID3 tags
    audio.tags.add(TIT2(encoding=3, text=chapter_title))
    audio.tags.add(TPE1(encoding=3, text=audiobook_author))
    audio.tags.add(TALB(encoding=3, text=audiobook_album))
    audio.tags.add(TRCK(encoding=3, text=str(i)))
    audio.tags.add(TYER(encoding=3, text=year))
    
    # Save the changes
    audio.save()
    
    print(f"{chapter_title} has been generated and saved with additional metadata to {mp3_filename}")

print("Audiobook chapters have been generated and saved with additional metadata.")