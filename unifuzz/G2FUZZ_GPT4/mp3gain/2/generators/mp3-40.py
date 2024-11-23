import os
from pydub import AudioSegment
from mutagen.id3 import ID3, TIT2, TPE1, TALB, TRCK, TCON, APIC

# Ensure the `./tmp/` directory exists
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

def generate_silent_segment(duration_ms):
    """
    Generate a silent audio segment of a given duration in milliseconds.
    """
    return AudioSegment.silent(duration=duration_ms)

# Define durations for a series of silent segments (in milliseconds)
durations = [1000, 2000, 1500, 2500]  # Different durations for variety

# Generate silent segments and combine them
combined_silent_audio = AudioSegment.empty()
for duration in durations:
    silent_segment = generate_silent_segment(duration)
    combined_silent_audio += silent_segment

# Define metadata for the combined track
metadata = {
    "title": "Combined Silent Track",
    "artist": "Anonymous",
    "album": "Combined Silence Album",
    "track_number": "1",
    "genre": "Silence",
}

# Define the path for the combined mp3 file
output_file_path = './tmp/combined_silent_track.mp3'

# Export the combined silent audio as an mp3 file
file_handle = combined_silent_audio.export(output_file_path, format="mp3")

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