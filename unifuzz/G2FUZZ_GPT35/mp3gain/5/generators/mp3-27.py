import os
import numpy as np
from PIL import Image
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, USLT, COMM
from pydub import AudioSegment

# Create a stereo channel mp3 file with Album Art, Lyrics, and Podcast Chapters Support
stereo_data = np.random.randn(2, 44100)  # Generating random stereo audio data
stereo_data = np.transpose(stereo_data)  # Transpose the data for pydub compatibility

audio = AudioSegment(stereo_data.tobytes(), frame_rate=44100, sample_width=2, channels=2)

# Save the stereo audio data to an MP3 file
audio.export('./tmp/stereo_with_album_art_lyrics_chapters.mp3', format='mp3')

# Add album art to the stereo mp3 file
audio_file = MP3('./tmp/stereo_with_album_art_lyrics_chapters.mp3', ID3=ID3)
audio_file.tags = ID3()

# Load album art
album_cover_path = '/experiments/outputs/mp3gain/mp3gain_FuzzGen/album_cover.jpg'

if os.path.exists(album_cover_path):
    image = Image.open(album_cover_path)

    with open(album_cover_path, 'rb') as album_art_file:
        album_art = album_art_file.read()

    # Add album art to the mp3 file
    apic = APIC(encoding=3, mime='image/jpeg', type=3, desc='Cover', data=album_art)
    audio_file.tags.add(apic)

    # Add lyrics to the mp3 file
    uslt_frame = USLT(encoding=3, lang='eng', desc='desc', text="Lyrics for the stereo audio file")
    audio_file.tags.add(uslt_frame)

    # Add Podcast Chapters to the mp3 file
    comm_frame = COMM(encoding=3, lang='eng', desc='Podcast Chapters', text="Chapter markers for easy navigation")
    audio_file.tags.add(comm_frame)

    audio_file.save()
else:
    print(f"Error: File '{album_cover_path}' not found.")