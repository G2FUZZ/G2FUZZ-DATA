import os

# Create a directory if it does not exist
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample mp3 file with more complex file features
sample_data = """
Audio Track 1: Main audio track with primary content.
Audio Track 2: Additional audio track with background music.
Audio Track 3: Bonus audio track with narration.
Embedded Images: Embedded images included for visualization.
Metadata: Various metadata tags added for detailed information (artist, album, genre, year).
Lyrics: Lyrics embedded in the mp3 file for sing-along experience.
Chapter Markers: Chapter markers set for easy navigation through the audio content.
Audio Effects: Audio effects applied for enhanced listening experience.
"""

file_path = './tmp/sample_complex_extended.mp3'

with open(file_path, 'w') as file:
    file.write(sample_data)

print(f"Generated extended complex mp3 file: {file_path}")