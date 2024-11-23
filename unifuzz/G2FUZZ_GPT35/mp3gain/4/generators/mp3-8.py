import numpy as np
from pydub import AudioSegment

# Generate random audio data
sample_rate = 44100
duration = 10  # seconds
num_samples = sample_rate * duration
audio_data = np.random.uniform(low=-1, high=1, size=num_samples)

# Convert audio data to bytes
audio_bytes = (audio_data * 32767).astype(np.int16).tobytes()

# Create AudioSegment object and export as mp3 file
audio = AudioSegment(data=audio_bytes, sample_width=2, frame_rate=sample_rate, channels=1)
audio.export("./tmp/good_balance_audio.mp3", format="mp3")