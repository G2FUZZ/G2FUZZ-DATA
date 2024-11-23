import os

# Create a directory if it does not exist
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample mp3 file with the provided features including Embedded subtitles
sample_data = """
Editable: MP3 files can be edited and manipulated using various software tools.
Variable sample rates: MP3 files can be encoded with variable sample rates to achieve different audio quality levels.
Embedded subtitles: Some MP3 files may include embedded subtitle tracks for displaying text during playback.
"""
file_path = './tmp/sample_extended.mp3'

with open(file_path, 'w') as file:
    file.write(sample_data)

print(f"Generated extended mp3 file: {file_path}")