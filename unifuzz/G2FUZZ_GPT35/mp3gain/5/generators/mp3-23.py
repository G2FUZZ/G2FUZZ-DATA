import numpy as np
import soundfile as sf
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TPE1, TCOM, ID3NoHeaderError

# Create a random audio signal
duration = 5  # 5 seconds
sampling_rate = 44100  # Default CD quality
num_samples = duration * sampling_rate
audio_signal = np.random.uniform(low=-1, high=1, size=num_samples)

# Save the audio signal as an mp3 file with extended metadata
output_path = './tmp/random_audio_extended.mp3'
sf.write(output_path, audio_signal, samplerate=sampling_rate, format='mp3')

# Add extended metadata
try:
    audio_file = MP3(output_path, ID3=ID3)
except ID3NoHeaderError:
    audio_file = MP3()
    audio_file.add_tags()

if audio_file.tags is None:
    audio_file.tags = ID3()

audio_file.tags.add(TPE1(encoding=3, text="Composer Name"))
audio_file.tags.add(TCOM(encoding=3, text="Conductor Name"))
audio_file.save(output_path)

print(f"MP3 file with extended metadata saved at {output_path}")