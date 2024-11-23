import numpy as np
from pydub import AudioSegment
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2, TPE1, APIC

# Create a stereo channel mp3 file with custom tags and album art
stereo_data_left = np.random.randn(44100)  # Generating random stereo audio data for left channel
stereo_data_right = np.random.randn(44100)  # Generating random stereo audio data for right channel
stereo_data = np.vstack((stereo_data_left, stereo_data_right))

# Convert stereo data to AudioSegment
stereo_audio = AudioSegment(stereo_data.tobytes(), frame_rate=44100, sample_width=2, channels=2)

# Save stereo audio to an MP3 file
stereo_audio.export('./tmp/stereo_with_custom_tags.mp3', format='mp3')

# Add custom tags and album art to the stereo mp3 file
audio_file = MP3('./tmp/stereo_with_custom_tags.mp3', ID3=ID3)
audio_file.tags = ID3()

audio_file.tags.add(TIT2(encoding=3, text="Custom Title"))
audio_file.tags.add(TPE1(encoding=3, text="Custom Artist"))

with open("album_art.jpg", "rb") as album_art_file:
    album_art_data = album_art_file.read()
    album_art = APIC(encoding=3, mime='image/jpeg', type=3, desc='Cover', data=album_art_data)
    audio_file.tags.add(album_art)

audio_file.save()