import os
from mutagen.mp3 import EasyMP3

file_path = "./tmp/sample.mp3"

# Check if the file exists
if os.path.exists(file_path):
    # Create a new MP3 file
    mp3_file = EasyMP3(file_path)

    # Set metadata
    mp3_file["artist"] = "John Doe"
    mp3_file["album"] = "My Album"
    mp3_file["title"] = "Sample Track"
    mp3_file["genre"] = "Pop"

    # Save the changes
    mp3_file.save()
else:
    print(f"Error: File '{file_path}' not found.")