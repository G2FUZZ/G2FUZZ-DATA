import numpy as np
import soundfile as sf
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3

# Create a random audio signal
duration = 5  # 5 seconds
sampling_rate = 44100  # Default CD quality
num_samples = duration * sampling_rate
audio_signal = np.random.uniform(low=-1, high=1, size=num_samples)

# Save the audio signal as an mp3 file without specifying bitrate
output_path = './tmp/random_audio_extended.mp3'
sf.write(output_path, audio_signal, samplerate=sampling_rate, format='mp3')

# Adding custom metadata to the mp3 file using mutagen
audio = MP3(output_path, ID3=EasyID3)
audio['artist'] = 'John Doe'
audio['album'] = 'Random Album'
audio['title'] = 'Random Song'
audio.save()

print(f"Extended MP3 file with sampling rate {sampling_rate} Hz saved at {output_path}")