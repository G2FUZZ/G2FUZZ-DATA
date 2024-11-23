import numpy as np
from scipy.io.wavfile import write
from pydub import AudioSegment
import os

# Ensure the tmp directory exists
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Generate a sine wave for the left channel
sample_rate = 44100  # Sample rate in Hz
duration = 5  # Duration in seconds
frequency_left = 440  # Frequency of the sine wave for the left channel in Hz
frequency_right = 444  # Frequency of the cosine wave for the right channel in Hz (binaural effect)
time = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
audio_left = np.sin(2 * np.pi * frequency_left * time) * 0.5
audio_right = np.cos(2 * np.pi * frequency_right * time) * 0.5

# Combine both channels
audio_stereo = np.vstack((audio_left, audio_right)).T  # Transpose to get stereo effect
audio_stereo = (audio_stereo * 32767).astype(np.int16)  # Convert to 16-bit PCM format

# Save the combined wave as a temporary WAV file
temp_wave_file = os.path.join(output_dir, "temp_stereo_audio.wav")
write(temp_wave_file, sample_rate, audio_stereo)

# Convert the WAV file to MP3 using pydub, demonstrating audio compression
audio_segment = AudioSegment.from_wav(temp_wave_file)
mp3_file = os.path.join(output_dir, "generated_stereo_audio.mp3")
audio_segment.export(mp3_file, format="mp3", bitrate="192k")  # Higher bitrate for better quality

# Clean up the temporary WAV file
os.remove(temp_wave_file)

print(f"Stereo MP3 file saved to: {mp3_file}")