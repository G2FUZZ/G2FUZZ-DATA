import numpy as np
import soundfile as sf
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, TIT2, TPE1

# Set the parameters for the audio file
duration = 5  # Duration of the audio file in seconds
sample_rate = 44100  # Sample rate in Hz
bit_depth = 16  # Bit depth of the audio file
artist = "Artist Name"
title = "Random Song Title"

# Generate random audio data
audio_data = np.random.randn(duration * sample_rate)

# Normalize the audio data based on the bit depth
max_val = 2 ** (bit_depth - 1) - 1
audio_data *= max_val / np.max(np.abs(audio_data))

# Save the audio data as an MP3 file with metadata
file_path = "./tmp/random_audio_complex.mp3"
sf.write(file_path, audio_data, sample_rate, format='MP3')

# Create a placeholder image file for album artwork
with open("./tmp/album_artwork.jpg", "wb") as album_art_file:
    album_art_file.write(b'Placeholder image data')

# Add metadata to the MP3 file
audio = MP3(file_path, ID3=ID3)
audio["TIT2"] = TIT2(encoding=3, text=title)
audio["TPE1"] = TPE1(encoding=3, text=artist)
with open("./tmp/album_artwork.jpg", "rb") as album_art_file:
    audio["APIC"] = APIC(
        encoding=3,
        mime="image/jpeg",
        type=3,
        desc="Cover",
        data=album_art_file.read()
    )
audio.save()

print(f"MP3 file with bit depth {bit_depth}, artist '{artist}', and title '{title}' saved at: {file_path}")