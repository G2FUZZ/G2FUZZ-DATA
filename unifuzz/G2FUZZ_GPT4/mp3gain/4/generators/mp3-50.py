import numpy as np
from scipy.io.wavfile import write
from pydub import AudioSegment
import os

# Ensure the tmp directory exists
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Function to generate a sine wave
def generate_sine_wave(freq, sample_rate, duration):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = np.sin(2 * np.pi * freq * t) * 0.5
    return (wave * 32767).astype(np.int16)

# Generate multiple sine waves for a chord
sample_rate = 44100  # Sample rate in Hz
duration = 5  # Duration in seconds
frequencies = [440, 550, 660]  # Frequencies of the sine waves in Hz to form a chord
waves = [generate_sine_wave(freq, sample_rate, duration) for freq in frequencies]

# Combine sine waves to form a chord
combined_wave = np.zeros(int(sample_rate * duration)).astype(np.int16)
for wave in waves:
    combined_wave = np.add(combined_wave, wave)
combined_wave = np.divide(combined_wave, len(frequencies)).astype(np.int16)  # Normalize volume

# Save the sine wave chord as a temporary WAV file
temp_wave_file = os.path.join(output_dir, "temp_chord_audio.wav")
write(temp_wave_file, sample_rate, combined_wave)

# Convert the WAV file to MP3 using pydub, demonstrating audio compression
audio_segment = AudioSegment.from_wav(temp_wave_file)

# Apply a fade-in of 2 seconds and a fade-out of 2 seconds
audio_segment_with_effects = audio_segment.fade_in(2000).fade_out(2000)

# Set metadata for the MP3 file
tags = {
    "artist": "Example Artist",
    "title": "Example Title",
    "album": "Example Album",
}

mp3_file = os.path.join(output_dir, "generated_chord_audio.mp3")
audio_segment_with_effects.export(mp3_file, format="mp3", bitrate="128k", tags=tags)

# Clean up the temporary WAV file
os.remove(temp_wave_file)

print(f"Generated MP3 file with complex features saved to: {mp3_file}")