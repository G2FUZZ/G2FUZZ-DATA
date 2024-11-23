import numpy as np
from scipy.io.wavfile import write
from pydub import AudioSegment
from pydub.effects import low_pass_filter
import os

# Ensure the tmp directory exists
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output,dir)

# Generate a sine wave as an example
sample_rate = 44100  # Sample rate in Hz
duration = 5  # Duration in seconds
frequency = 440  # Frequency of the sine wave in Hz
time = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
audio = np.sin(2 * np.pi * frequency * time) * 0.5
audio = (audio * 32767).astype(np.int16)  # Convert to 16-bit PCM format

# Save the sine wave as a temporary WAV file
temp_wave_file = os.path.join(output_dir, "temp_audio.wav")
write(temp_wave_file, sample_rate, audio)

# Convert the WAV file to MP3 using pydub, demonstrating audio compression
audio_segment = AudioSegment.from_wav(temp_wave_file)

# Apply a lowpass filter with adjustable cutoff
# Adjust the cutoff frequency as needed. Example: 5000 Hz
cutoff_frequency = 5000  # Frequency in Hz
filtered_audio_segment = low_pass_filter(audio_segment, cutoff_frequency)

mp3_file = os.path.join(output_dir, "generated_audio_with_lowpass_filter.mp3")

# Export the filtered audio segment to MP3
filtered_audio_segment.export(mp3_file, format="mp3", bitrate="128k")

# Clean up the temporary WAV file
os.remove(temp_wave_file)

print(f"Generated MP3 file with lowpass filter saved to: {mp3_file}")