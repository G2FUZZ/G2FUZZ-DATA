import soundfile as sf
import numpy as np
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2, TPE1

# Create a stereo channel mp3 file with Custom Metadata
stereo_data_left = np.random.randn(44100)  # Generating random left channel audio data
stereo_data_right = np.random.randn(44100)  # Generating random right channel audio data
stereo_data = np.vstack((stereo_data_left, stereo_data_right))

sf.write('./tmp/stereo_with_custom_metadata.mp3', stereo_data.T, samplerate=44100)

# Add custom metadata to the stereo mp3 file
audio_file = MP3('./tmp/stereo_with_custom_metadata.mp3', ID3=ID3)
audio_file.tags = ID3()

# Add custom title and artist information to the mp3 file
title_frame = TIT2(encoding=3, text="Custom Title")
artist_frame = TPE1(encoding=3, text="Custom Artist")
audio_file.tags.add(title_frame)
audio_file.tags.add(artist_frame)

audio_file.save()