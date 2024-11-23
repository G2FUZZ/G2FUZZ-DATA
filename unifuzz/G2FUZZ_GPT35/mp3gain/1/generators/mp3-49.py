import os

# Create a directory if it does not exist
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample mp3 file with more complex file features
sample_data = """
Audio Track 1: Main audio track with vocals.
Audio Track 2: Instrumental version of the main track.
Audio Track 3: Acapella version of the main track.
Embedded Images: Album cover and artist images embedded.
Metadata: Detailed metadata including artist, album, genre, year, composer, lyrics, and comments.
"""
file_path = './tmp/sample_complex_extended.mp3'

with open(file_path, 'w') as file:
    file.write(sample_data)

print(f"Generated extended complex mp3 file: {file_path}")