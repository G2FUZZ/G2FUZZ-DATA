import os
from pydub import AudioSegment
from pydub.generators import Sine, WhiteNoise

# Ensure the './tmp/' directory exists
os.makedirs('./tmp/', exist_ok=True)

# Function to generate a sine wave audio segment
def generate_sine_wave(frequency, duration_in_ms, volume):
    return Sine(frequency).to_audio_segment(duration=duration_in_ms, volume=volume)

# Generate multiple sine waves for a chord (A major chord: A, C#, and E)
frequencies = [440, 554.37, 659.25]  # Frequencies for A4, C#5, and E5 notes
duration_in_ms = 5000  # Duration in milliseconds
volume = -20.0  # Volume in dB

# Generate sine waves and overlay them to create a chord
chord = AudioSegment.silent(duration=duration_in_ms)
for freq in frequencies:
    sine_wave = generate_sine_wave(freq, duration_in_ms, volume)
    chord = chord.overlay(sine_wave)

# Add a fade-in and fade-out effect (1 second each)
fade_duration = 1000  # 1 second in milliseconds
chord = chord.fade_in(fade_duration).fade_out(fade_duration)

# Generate and overlay white noise for texture, at a lower volume
noise_volume = -40.0  # Lower volume for the noise
white_noise = WhiteNoise().to_audio_segment(duration=duration_in_ms, volume=noise_volume)
chord_with_noise = chord.overlay(white_noise)

# Export the generated audio with a constant bitrate
file_path = './tmp/complex_generated_audio.mp3'
# Use a common constant bitrate (CBR) for MP3
chord_with_noise.export(file_path, format="mp3", bitrate="192k")

print(f"Generated mp3 file with a complex texture at {file_path}")