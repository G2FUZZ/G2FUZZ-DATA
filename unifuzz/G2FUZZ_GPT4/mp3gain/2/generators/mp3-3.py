import os
from pydub import AudioSegment
from mutagen.id3 import ID3, TIT2, TPE1, TALB, TRCK, TCON, APIC

# Ensure the `./tmp/` directory exists
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Generate a silent audio segment (1 second long)
silent_audio = AudioSegment.silent(duration=1000)  # 1000ms = 1 second

# Define metadata
metadata = {
    "title": "Silent Track",
    "artist": "Anonymous",
    "album": "Silence Album",
    "track_number": "1",
    "genre": "Silence",
}

# Define the path for the mp3 file
output_file_path = './tmp/silent_track.mp3'

# Export the silent audio as an mp3 file
file_handle = silent_audio.export(output_file_path, format="mp3")

# Now, we'll add ID3 metadata to the mp3 file
audio = ID3(output_file_path)

# Adding/Updating metadata
audio.add(TIT2(encoding=3, text=metadata["title"]))
audio.add(TPE1(encoding=3, text=metadata["artist"]))
audio.add(TALB(encoding=3, text=metadata["album"]))
audio.add(TRCK(encoding=3, text=metadata["track_number"]))
audio.add(TCON(encoding=3, text=metadata["genre"]))

# Save the changes
audio.save()