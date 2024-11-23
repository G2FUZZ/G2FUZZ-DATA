import numpy as np
import pydub
from pydub.generators import Sine, Square, Sawtooth
import os

# Ensure the tmp directory exists
os.makedirs('./tmp', exist_ok=True)

# Define a function to generate a sine, square, and sawtooth wave, then save them as an MP3 with various effects
def generate_complex_mp3(frequency=440, duration_seconds=5, volume=-20.0, sample_rate=44100):
    # Generate different waveforms
    sine_wave = Sine(frequency).to_audio_segment(duration=duration_seconds * 1000, volume=volume)
    square_wave = Square(frequency).to_audio_segment(duration=duration_seconds * 1000, volume=volume)
    sawtooth_wave = Sawtooth(frequency).to_audio_segment(duration=duration_seconds * 1000, volume=volume)
    
    # Apply a fade-in effect to each waveform
    fade_duration = 2000  # 2 seconds
    sine_wave = sine_wave.fade_in(fade_duration)
    square_wave = square_wave.fade_in(fade_duration)
    sawtooth_wave = sawtooth_wave.fade_in(fade_duration)
    
    # Combine the waveforms into a single track, with a pan effect
    combined_wave = sine_wave.pan(-1) + square_wave.pan(0) + sawtooth_wave.pan(1)  # Left, center, right pan
    
    # Export the combined waveforms as an mp3
    combined_wave.export('./tmp/complex_waveform.mp3', format='mp3', bitrate='192k')

    # Generate a sequence of frequencies to create a more complex sound pattern
    frequencies = np.linspace(frequency, frequency * 2, 5)  # Example: from 440 Hz to 880 Hz
    complex_sound = None
    for freq in frequencies:
        temp_wave = Sine(freq).to_audio_segment(duration=duration_seconds * 1000 / len(frequencies), volume=volume).fade_in(200)
        complex_sound = temp_wave if complex_sound is None else complex_sound + temp_wave
    
    # Export the complex sound pattern as an mp3
    complex_sound.export('./tmp/complex_sound_pattern.mp3', format='mp3', bitrate='192k')

# Execute the function to generate the mp3 files
generate_complex_mp3()