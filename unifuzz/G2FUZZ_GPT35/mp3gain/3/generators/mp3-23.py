import numpy as np
import soundfile as sf

# Set the parameters for the audio file
duration = 5  # Duration of the audio file in seconds
sample_rate = 44100  # Sample rate in Hz
bit_depth = 16  # Bit depth of the audio file

# Generate random audio data
audio_data = np.random.randn(duration * sample_rate)

# Normalize the audio data based on the bit depth
max_val = 2 ** (bit_depth - 1) - 1
audio_data *= max_val / np.max(np.abs(audio_data))

# Save the audio data as an MP3 file
file_path = "./tmp/random_audio.mp3"
sf.write(file_path, audio_data, sample_rate, format='MP3')
print(f"MP3 file with bit depth {bit_depth} saved at: {file_path}")