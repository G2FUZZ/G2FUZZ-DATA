import numpy as np
from pydub import AudioSegment
from pydub.generators import Sine, WhiteNoise
import os
import random
from pydub import effects  # Ensure effects is correctly imported

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

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

# Parameters for the audio structure
intro_frequencies = [440, 550, 660]
verse_frequencies = [770, 880, 990]
outro_frequencies = [1100, 1210, 1320]
section_durations = [2000, 3000, 2000]  # milliseconds

# Generate sections
intro_left = generate_tone_sequence(intro_frequencies, section_durations, amplitude=0.5)
verse_left = generate_tone_sequence(verse_frequencies, section_durations, amplitude=0.7)
outro_left = generate_tone_sequence(outro_frequencies, section_durations, amplitude=0.5)

intro_right = generate_tone_sequence([x+2 for x in intro_frequencies], section_durations, amplitude=0.5)
verse_right = generate_tone_sequence([x+2 for x in verse_frequencies], section_durations, amplitude=0.7)
outro_right = generate_tone_sequence([x+2 for x in outro_frequencies], section_durations, amplitude=0.5)

# Combine sections with random noise added
left_channel = add_random_noise(intro_left + verse_left + outro_left, intensity=0.02)
right_channel = add_random_noise(intro_right + verse_right + outro_right, intensity=0.02)

# Normalize and combine the two channels to create a stereo signal
left_channel = effects.normalize(left_channel)
right_channel = effects.normalize(right_channel)
stereo_sound = AudioSegment.from_mono_audiosegments(left_channel, right_channel)

# Export with joint stereo and lowpass filter settings
stereo_sound.export('./tmp/complex_stereo_example.mp3', format='mp3', parameters=["-joint_stereo", "1", "-af", "lowpass=f=15000"])

print("Complex MP3 file with multiple sine waves and random noise has been generated at './tmp/complex_stereo_example.mp3'")