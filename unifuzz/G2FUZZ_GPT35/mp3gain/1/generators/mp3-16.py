import os

# Create a directory if it does not exist
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample mp3 file with the provided features
sample_data = "Editable: MP3 files can be edited and manipulated using various software tools.\nEmbedded URLs: MP3 files may contain embedded URLs linking to related content or websites."
file_path = './tmp/sample_with_urls.mp3'

with open(file_path, 'w') as file:
    file.write(sample_data)

print(f"Generated mp3 file with Embedded URLs: {file_path}")