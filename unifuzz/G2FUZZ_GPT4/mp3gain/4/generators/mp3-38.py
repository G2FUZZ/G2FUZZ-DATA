import numpy as np
from pydub import AudioSegment
from pydub.generators import Sine
import os

def generate_sine_wave(frequency, duration_ms, volume=-20.0):
    """
    Generates a sine wave of a specified frequency and duration.

    Parameters:
    frequency (float): Frequency of the sine wave in Hz.
    duration_ms (int): Duration of the sine wave in milliseconds.
    volume (float): Volume adjustment in dB.

    Returns:
    AudioSegment: The generated sine wave as an audio segment.
    """
    sine_wave = Sine(frequency).to_audio_segment(duration=duration_ms).apply_gain(volume)
    return sine_wave

def generate_chord(frequencies, duration_ms, volume=-20.0):
    """
    Generates a chord from multiple sine waves.

    Parameters:
    frequencies (list of float): Frequencies of the sine waves in Hz.
    duration_ms (int): Duration of the chord in milliseconds.
    volume (float): Volume adjustment in dB for the chord.

    Returns:
    AudioSegment: The generated chord as an audio segment.
    """
    chord = AudioSegment.silent(duration=duration_ms)
    for freq in frequencies:
        chord = chord.overlay(generate_sine_wave(freq, duration_ms, volume))
    return chord

def generate_melody(chords, duration_ms, volume=-20.0):
    """
    Generates a melody by sequencing chords.

    Parameters:
    chords (list of list of float): Each element is a list of frequencies representing a chord.
    duration_ms (int): Duration of each chord in the melody in milliseconds.
    volume (float): Volume adjustment in dB for the melody.

    Returns:
    AudioSegment: The generated melody as an audio segment.
    """
    melody = AudioSegment.silent(duration=0)
    for chord_freqs in chords:
        chord = generate_chord(chord_freqs, duration_ms, volume)
        melody += chord
    return melody

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define a simple melody using chords (C major, F major, G major, C major)
chords = [
    [261.63, 329.63, 392.00],  # C major
    [349.23, 440.00, 523.25],  # F major
    [392.00, 493.88, 587.33],  # G major
    [261.63, 329.63, 392.00]   # C major
]

# Generate the melody
melody = generate_melody(chords, duration_ms=1000, volume=-10.0)

# Save the generated melody to a file
melody_file_path = './tmp/melody.mp3'
melody.export(melody_file_path, format="mp3")

print(f"Melody file saved to '{melody_file_path}'")