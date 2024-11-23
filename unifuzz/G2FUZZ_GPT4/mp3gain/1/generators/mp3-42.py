from pydub import AudioSegment
from pydub.generators import Sine, Square, Sawtooth
import numpy as np
import os

# Ensure the tmp directory exists
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Generate different waveforms with a 5-second duration at 440 Hz
tone_duration_ms = 5000  # Duration in milliseconds
frequency_hz = 440  # Frequency in Hertz

# Generate different waveforms
sine_wave = Sine(frequency_hz).to_audio_segment(duration=tone_duration_ms)
square_wave = Square(frequency_hz).to_audio_segment(duration=tone_duration_ms)
sawtooth_wave = Sawtooth(frequency_hz).to_audio_segment(duration=tone_duration_ms)

# Apply a fade-in effect to each waveform
fade_duration = 2000  # 2 seconds
sine_wave = sine_wave.fade_in(fade_duration)
square_wave = square_wave.fade_in(fade_duration)
sawtooth_wave = sawtooth_wave.fade_in(fade_duration)

# Combine the waveforms into a single track, with a pan effect
combined_wave = sine_wave.pan(-1) + square_wave.pan(0) + sawtooth_wave.pan(1)  # Left, center, right pan

# Export the combined waveforms as an mp3
file_path_combined = './tmp/complex_waveform.mp3'
combined_wave.export(file_path_combined, format='mp3', bitrate='192k')

# Generate a sequence of frequencies to create a more complex sound pattern
frequencies = np.linspace(frequency_hz, frequency_hz * 2, 5)  # Example: from 440 Hz to 880 Hz
complex_sound = None
for freq in frequencies:
    temp_wave = Sine(freq).to_audio_segment(duration=tone_duration_ms / len(frequencies)).fade_in(200)
    complex_sound = temp_wave if complex_sound is None else complex_sound + temp_wave

# Export the complex sound pattern as an mp3
file_path_complex = './tmp/complex_sound_pattern.mp3'
complex_sound.export(file_path_complex, format='mp3', bitrate='192k')

print(f"Files have been saved to {file_path_combined} and {file_path_complex}")