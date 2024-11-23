import os
import numpy as np
from pydub import AudioSegment
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC

# Generate random audio data
sample_rate = 44100
duration = 10  # seconds
num_samples = sample_rate * duration
audio_data = np.random.uniform(low=-1, high=1, size=num_samples)

# Convert audio data to bytes
audio_bytes = (audio_data * 32767).astype(np.int16).tobytes()

# Create AudioSegment object
audio = AudioSegment(data=audio_bytes, sample_width=2, frame_rate=sample_rate, channels=1)

# Add embedded album art
mp3_file_path = "./tmp/good_balance_audio_with_album_art.mp3"
audio.export(mp3_file_path, format="mp3")

# Embed album art
audio_file = MP3(mp3_file_path, ID3=ID3)
album_art_path = "album_art.jpg"

if os.path.exists(album_art_path):
    with open(album_art_path, "rb") as album_art_file:
        album_art = album_art_file.read()
    audio_file.tags.add(APIC(encoding=3, mime='image/jpeg', type=3, desc=u'Cover', data=album_art))
    audio_file.save()
else:
    print(f"Error: File '{album_art_path}' not found.")