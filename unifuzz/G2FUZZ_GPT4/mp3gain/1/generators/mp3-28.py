from pydub import AudioSegment
from pydub.generators import Sine
import numpy as np
import os

def change_pitch(audio_segment, octaves):
    """
    Changes the pitch of an audio segment without changing its duration.

    :param audio_segment: The audio segment to modify.
    :param octaves: The number of octaves to shift the pitch. Positive values raise the pitch, negative values lower it.
    :return: A new audio segment with the modified pitch.
    """
    new_sample_rate = int(audio_segment.frame_rate * (2.0 ** octaves))
    # Use the corrected variable name
    return audio_segment._spawn(audio_segment.raw_data, overrides={'frame_rate': new_sample_rate})

# Ensure the tmp directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Generate a 440 Hz sine wave (A4 note) for 5 seconds
frequency = 440  # Frequency in Hz
duration = 5000  # Duration in milliseconds
volume = -20.0  # Volume in dB

# Generate sine wave
tone = Sine(frequency, sample_rate=44100).to_audio_segment(duration=duration, volume=volume)

# Apply pitch control
octaves = 0.5  # Raise the pitch by half an octave
pitch_controlled_tone = change_pitch(tone, octaves)

# Save the generated tone with pitch control as an MP3 file
output_path = os.path.join(output_dir, 'generated_tone_with_pitch_control.mp3')
pitch_controlled_tone.export(output_path, format="mp3", bitrate="128k")

print(f"MP3 file with pitch control saved to {output_path}")