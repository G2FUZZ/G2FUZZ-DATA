import os
from pydub import AudioSegment
from mutagen.id3 import ID3, TIT2, TPE1, TALB, TRCK, TCON, APIC, TDRC

# Ensure the `./tmp/` directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def create_silent_track(duration, track_number, metadata, album_art_path=None):
    """
    Creates a silent track with specified duration and metadata, optionally embedding album art.
    :param duration: Duration of silence in milliseconds.
    :param track_number: Track number as a string.
    :param metadata: Dictionary containing metadata fields.
    :param album_art_path: Path to the album art image file.
    """
    silent_audio = AudioSegment.silent(duration=duration)

    # Define the path for the mp3 file
    output_file_path = os.path.join(output_dir, f"track_{track_number}.mp3")

    # Export the silent audio as an mp3 file
    silent_audio.export(output_file_path, format="mp3", bitrate="192k")

    # Now, we'll add ID3 metadata to the mp3 file, including album art if provided
    audio = ID3(output_file_path)

    # Adding/Updating basic metadata
    audio.add(TIT2(encoding=3, text=metadata["title"]))
    audio.add(TPE1(encoding=3, text=metadata["artist"]))
    audio.add(TALB(encoding=3, text=metadata["album"]))
    audio.add(TRCK(encoding=3, text=str(track_number)))
    audio.add(TCON(encoding=3, text=metadata["genre"]))
    audio.add(TDRC(encoding=3, text=metadata["year"]))

    # Adding album art if the path is provided and the file exists
    if album_art_path and os.path.exists(album_art_path):
        with open(album_art_path, 'rb') as img:
            audio.add(APIC(3, 'image/jpeg', 3, 'Front cover', img.read()))
    else:
        print(f"Album art file not found at {album_art_path}")

    # Save the changes
    audio.save()

# Example usage
metadata = {
    "title": "Silent Track",
    "artist": "Anonymous",
    "album": "Silence Album",
    "genre": "Silence",
    "year": "2023"
}

# Generate multiple tracks with varying durations
durations = [1000, 2000, 3000]  # Durations in milliseconds

for i, duration in enumerate(durations, start=1):
    create_silent_track(duration, i, metadata, album_art_path='./path/to/album_art.jpg')