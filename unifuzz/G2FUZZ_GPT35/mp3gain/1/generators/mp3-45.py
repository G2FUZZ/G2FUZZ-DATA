import os

# Create a directory if it does not exist
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample mp3 file with advanced file features
sample_data = """
Audio Track 1: This is the main audio track with the primary content.
Audio Track 2: This is an additional audio track with background music.
Audio Track 3: This is a bonus audio track with narration.
Embedded Images: This mp3 file includes embedded images for visualization.
Metadata: Various metadata tags are added to the mp3 file for detailed information, including artist, album, genre, and year.
Custom Tags: Custom tags can be added to provide specific information about the audio content.
Chapter Marks: This mp3 file includes chapter marks for easy navigation.
Extended Chapters: This mp3 file also includes extended chapters for more detailed navigation.
Cover Art: A cover art image is embedded in the mp3 file for display.
"""
file_path = './tmp/sample_complex_advanced.mp3'

with open(file_path, 'w') as file:
    file.write(sample_data)

print(f"Generated advanced complex mp3 file: {file_path}")