import os

# Create a directory if it does not exist
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample mp3 file with the provided features
sample_data = """
Editable: MP3 files can be edited and manipulated using various software tools.
Cue points: Some MP3 files can contain cue points for specifying specific playback positions or sections within the audio.
"""
file_path = './tmp/sample_with_cue_points.mp3'

with open(file_path, 'w') as file:
    file.write(sample_data)

print(f"Generated mp3 file with Cue points: {file_path}")