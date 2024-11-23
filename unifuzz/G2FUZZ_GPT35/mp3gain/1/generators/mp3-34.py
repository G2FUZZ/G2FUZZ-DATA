import os

# Create a directory if it does not exist
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample mp3 file with more complex file structures
sample_data = """
Audio Track 1: This is the main audio track with the primary content.
Audio Track 2: This is an additional audio track with background music.
Embedded Images: This mp3 file includes embedded images for visualization.
Metadata: Various metadata tags are added to the mp3 file for detailed information.
"""
file_path = './tmp/sample_complex.mp3'

with open(file_path, 'w') as file:
    file.write(sample_data)

print(f"Generated complex mp3 file: {file_path}")