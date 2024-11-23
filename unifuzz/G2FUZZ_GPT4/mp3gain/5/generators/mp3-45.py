from pydub import AudioSegment
from pydub.generators import Sine, WhiteNoise
from pydub import effects  # Ensure effects is correctly imported
import os
import random

# Ensure the tmp directory exists
os.makedirs('./tmp', exist_ok=True)

def generate_tone_sequence(frequencies, durations, amplitude=0.5):
    """
    Generate a sequence of tones.
    :param frequencies: List of frequencies for each tone.
    :param durations: List of durations for each tone (milliseconds).
    :param amplitude: Amplitude of the tones (0.0 to 1.0).
    :return: Combined AudioSegment of the sequence.
    """
    sequence = AudioSegment.silent(duration=0)
    for freq, dur in zip(frequencies, durations):
        tone = Sine(freq, sample_rate=44100).to_audio_segment(duration=dur).apply_gain(-20 + (amplitude * 20))
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

# Parameters for the audio
duration_in_seconds = 10  # Duration of the audio file in seconds
frequencies = [440, 550, 660]  # Frequencies for tone sequence
durations = [duration_in_seconds * 1000 // len(frequencies)] * len(frequencies)  # Evenly split duration
amplitude = 0.5  # Amplitude for tone sequence

# Generate a sequence of tones
tone_sequence = generate_tone_sequence(frequencies, durations, amplitude=amplitude)

# Add random noise to the tone sequence
tone_sequence_with_noise = add_random_noise(tone_sequence, intensity=0.02)

# Normalize the audio
normalized_tone_sequence = effects.normalize(tone_sequence_with_noise)

# Bit rates to generate MP3 files for
bit_rates = ['8k', '128k', '320k']

for bit_rate in bit_rates:
    # Define the file path
    file_path = f'./tmp/complex_tone_sequence_{bit_rate}.mp3'
    
    # Export the normalized tone sequence to an MP3 file with the specified bit rate
    normalized_tone_sequence.export(file_path, format="mp3", bitrate=bit_rate)

    print(f"Generated MP3 file with a complex tone sequence and random noise at {bit_rate} bitrate: {file_path}")