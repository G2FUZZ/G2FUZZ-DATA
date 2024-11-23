import os

# Create a directory if it does not exist
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample mp3 file with the provided features including Embedded subtitles and Embedded images
sample_data = """
Editable: MP3 files can be edited and manipulated using various software tools.
Variable sample rates: MP3 files can be encoded with variable sample rates to achieve different audio quality levels.
Embedded subtitles: Some MP3 files may include embedded subtitle tracks for displaying text during playback.
Embedded images: MP3 files can embed images such as cover art, artist photos, or visual content related to the audio.
"""
file_path = './tmp/sample_extended_with_images.mp3'

with open(file_path, 'w') as file:
    file.write(sample_data)

print(f"Generated extended mp3 file with images: {file_path}")