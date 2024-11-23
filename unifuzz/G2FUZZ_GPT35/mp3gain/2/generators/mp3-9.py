import numpy as np
import soundfile as sf

# Create a dummy audio signal
sample_rate = 44100  # Sample rate of 44.1 kHz for CD quality audio
duration = 5  # Duration of the audio signal in seconds
bit_depth = 16  # Bit depth of the audio signal

num_samples = int(sample_rate * duration)
audio_signal = np.random.uniform(low=-1, high=1, size=num_samples)

# Save the audio signal as a WAV file
file_path = './tmp/generated_audio.wav'
sf.write(file_path, audio_signal, sample_rate, subtype='PCM_' + str(bit_depth))