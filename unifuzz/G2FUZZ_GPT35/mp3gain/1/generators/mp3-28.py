import os

# Create a directory if it does not exist
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample mp3 file with the provided features including Chapter markers and Network streaming metadata
sample_data = """Editable: MP3 files can be edited and manipulated using various software tools.
Chapter markers: MP3 files can contain chapter markers for easy navigation within long audio files or audiobooks.
Network streaming metadata: MP3 files can include metadata specific to streaming services, such as track popularity or recommendations."""
file_path = './tmp/sample_with_all_features.mp3'

with open(file_path, 'w') as file:
    file.write(sample_data)

print(f"Generated mp3 file with all features: {file_path}")