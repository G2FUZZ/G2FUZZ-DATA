import os
from mutagen.mp3 import MP3

file_path = "./tmp/extended_sample.mp3"

# Check if the file exists
if os.path.exists(file_path):
    # Create a new MP3 file
    mp3_file = MP3(file_path)

    # Set metadata
    mp3_file["artist"] = ["John Doe", "Jane Smith"]
    mp3_file["album"] = "Extended Album"
    mp3_file["title"] = "Extended Sample Track"
    mp3_file["genre"] = "Pop"
    mp3_file["comment"] = "This is a custom comment for the track"
    mp3_file["tracknumber"] = "02/12"

    # Save the changes
    mp3_file.save()
else:
    print(f"Error: File '{file_path}' not found.")