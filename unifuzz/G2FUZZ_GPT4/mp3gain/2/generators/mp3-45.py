import os
from pydub import AudioSegment
from mutagen.id3 import ID3, TIT2, TPE1, TALB, TRCK, TCON, APIC, ID3NoHeaderError

# Ensure the `./tmp/` directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate a silent audio segment (1 second long)
silent_audio = AudioSegment.silent(duration=1000)  # 1000ms = 1 second

def generate_silent_mp3_with_metadata(output_file_path, metadata, cover_art_path=None):
    # Export the silent audio as an mp3 file
    silent_audio.export(output_file_path, format="mp3")
    
    # Attempt to add ID3 tags to the MP3 file
    try:
        audio = ID3(output_file_path)
    except ID3NoHeaderError:
        audio = ID3()
    
    # Adding/Updating metadata with more details
    audio.add(TIT2(encoding=3, text=metadata["title"]))
    audio.add(TPE1(encoding=3, text=metadata["artist"]))
    audio.add(TALB(encoding=3, text=metadata["album"]))
    audio.add(TRCK(encoding=3, text=metadata["track_number"]))
    audio.add(TCON(encoding=3, text=metadata["genre"]))
    
    # Adding cover art if the path is provided and the file exists
    if cover_art_path and os.path.exists(cover_art_path):
        with open(cover_art_path, 'rb') as img:
            audio.add(APIC(encoding=3, mime='image/jpeg', type=3, desc='Cover', data=img.read()))
    elif cover_art_path:
        print(f"Cover art file not found at {cover_art_path}. Skipping cover art addition.")

    # Save the changes with enhanced metadata and optional cover art
    audio.save()

# Define metadata
metadata = {
    "title": "Silent Track",
    "artist": "Anonymous",
    "album": "Silence Album",
    "track_number": "1",
    "genre": "Silence",
}

# Define the path for the mp3 file and optional cover art
output_file_path = './tmp/silent_track.mp3'
cover_art_path = './path/to/cover_art.jpg'  # Update this path as necessary

# Call the function with the provided metadata and cover art path
generate_silent_mp3_with_metadata(output_file_path, metadata, cover_art_path)