import os
import numpy as np
from pydub import AudioSegment
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC
from pydub.generators import Pulse

# Generate a simple pulse audio signal
audio = Pulse(440).to_audio_segment(duration=10000)  # 10 seconds of a pulse wave at 440 Hz

# Add embedded album art
mp3_file_path = "./tmp/sample_pulse_audio_with_album_art.mp3"
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