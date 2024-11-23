import numpy as np
from pydub import AudioSegment

# Create a dummy audio signal
sample_rate = 44100  # Sample rate of 44.1 kHz for CD quality audio
duration = 5  # Duration of the audio signal in seconds
bit_depth = 16  # Bit depth of the audio signal

num_samples = int(sample_rate * duration)
audio_signal = np.random.uniform(low=-1, high=1, size=num_samples)

# Convert the audio signal to an MP3 file with Gapless metadata
file_path = './tmp/generated_audio.mp3'
audio_signal_int = np.int16(audio_signal * 32767)  # Convert to 16-bit integer
audio = AudioSegment(audio_signal_int.tobytes(), frame_rate=sample_rate, sample_width=2, channels=1)
audio.export(file_path, format="mp3", tags={"artist": "Unknown", "title": "Generated Audio", "gapless": "true"})