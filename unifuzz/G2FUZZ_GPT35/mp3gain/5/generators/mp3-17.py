import soundfile as sf
import numpy as np
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, USLT, COMM

# Create a mono channel mp3 file with Lyrics and Podcast Chapters Support
mono_data = np.random.randn(44100)  # Generating random mono audio data
sf.write('./tmp/mono_with_lyrics_and_chapters.mp3', mono_data, samplerate=44100)

# Add lyrics to the mono mp3 file
audio_file = MP3('./tmp/mono_with_lyrics_and_chapters.mp3', ID3=ID3)
audio_file.tags = ID3()

# Add lyrics to the mp3 file
uslt_frame = USLT(encoding=3, lang='eng', desc='desc', text="Lyrics for the mono audio file")
audio_file.tags.add(uslt_frame)

# Add Podcast Chapters to the mp3 file
comm_frame = COMM(encoding=3, lang='eng', desc='Podcast Chapters', text="Chapter markers for easy navigation")
audio_file.tags.add(comm_frame)

audio_file.save()