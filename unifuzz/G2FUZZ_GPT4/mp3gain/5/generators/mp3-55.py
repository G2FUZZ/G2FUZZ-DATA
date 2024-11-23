import numpy as np
from pydub import AudioSegment
from pydub.generators import Sine, WhiteNoise
import os
from pydub import effects  # Ensure effects is correctly imported

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

def generate_tone_sequence(frequencies, durations, amplitude=0.5, sample_rate=44100):
    """
    Generate a sequence of tones.
    :param frequencies: List of frequencies for each tone.
    :param durations: List of durations for each tone in seconds.
    :param amplitude: Amplitude of the tones (0.0 to 1.0).
    :param sample_rate: Sample rate in Hz.
    :return: Combined AudioSegment of the sequence.
    """
    sequence = AudioSegment.silent(duration=0)
    for freq, dur in zip(frequencies, durations):
        tone = Sine(freq, sample_rate=sample_rate).to_audio_segment(duration=int(dur*1000)).apply_gain(-20 + (amplitude * 20))
        sequence += tone
    return sequence

def add_random_noise(segment, intensity=0.01):
    """
    Add random noise to an audio segment.
    :param segment: AudioSegment to add noise to.
    :param intensity: Intensity of the noise (0.0 to 1.0).
    :return: AudioSegment with added noise.
    """
    noise = WhiteNoise().to_audio_segment(duration=len(segment))
    noise = noise - (20 - (intensity * 20))
    return segment.overlay(noise)

def save_to_mp3(audio_segment, filename):
    """
    Save audio data to an MP3 file.

    :param audio_segment: AudioSegment containing audio data to save
    :param filename: Filename for the MP3 file
    """
    # Export the audio segment to an MP3 file
    audio_segment.export(filename, format="mp3")

# Frequencies and durations for a simple melody
frequencies = [440, 550, 660, 770, 880]
durations = [1, 1, 1, 1, 1]  # in seconds

# Generate and save sequences with added noise for different sample rates
sampling_rates = [44100, 48000]

for sample_rate in sampling_rates:
    # Generate a sequence of tones
    sequence = generate_tone_sequence(frequencies, durations, amplitude=0.5, sample_rate=sample_rate)
    # Add random noise
    sequence_with_noise = add_random_noise(sequence, intensity=0.02)
    # Normalize
    normalized_sequence = effects.normalize(sequence_with_noise)
    # Save the sequence to an MP3 file
    filename = f'./tmp/melody_with_noise_{sample_rate/1000}kHz.mp3'
    save_to_mp3(normalized_sequence, filename)
    print(f'Generated MP3 file with melody and noise at {sample_rate/1000} kHz sampling rate at {filename}')