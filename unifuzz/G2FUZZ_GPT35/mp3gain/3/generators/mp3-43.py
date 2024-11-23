import numpy as np
import soundfile as sf
from pydub import AudioSegment

# Set the parameters for the audio file
duration = 5  # Duration of the audio file in seconds
sample_rate = 44100  # Sample rate in Hz
bit_depth = 16  # Bit depth of the audio file

# Generate random audio data for two stereo channels
audio_data_left = np.random.randn(duration * sample_rate)
audio_data_right = np.random.randn(duration * sample_rate)

# Normalize the audio data based on the bit depth
max_val = 2 ** (bit_depth - 1) - 1
audio_data_left *= max_val / np.max(np.abs(audio_data_left))
audio_data_right *= max_val / np.max(np.abs(audio_data_right))

# Combine stereo audio channels
audio_data_stereo = np.column_stack((audio_data_left, audio_data_right))

# Save the stereo audio data as a WAV file
file_path = "./tmp/random_audio_stereo.wav"
sf.write(file_path, audio_data_stereo, sample_rate)

# Add metadata to the WAV file
audio_segment = AudioSegment.from_file(file_path, format="wav")
audio_segment.export(file_path, format="mp3", tags={"artist": "Random Artist", "title": "Random Title"})

print(f"Stereo WAV file with bit depth {bit_depth} and metadata saved at: {file_path}")