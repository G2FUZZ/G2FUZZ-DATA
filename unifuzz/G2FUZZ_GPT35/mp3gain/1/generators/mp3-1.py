import os

# Create a directory to store the mp3 files
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample mp3 file
sample_mp3 = """
MP3 files use lossy compression to reduce file size while maintaining audio quality.
"""

filename = "./tmp/sample.mp3"

with open(filename, 'w') as file:
    file.write(sample_mp3)

print(f"Generated mp3 file: {filename}")