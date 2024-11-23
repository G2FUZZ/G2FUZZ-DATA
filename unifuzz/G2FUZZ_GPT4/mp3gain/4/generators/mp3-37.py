import numpy as np
from pydub import AudioSegment
from pydub.generators import Sine, Square, Sawtooth
import os

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate a 1-second sine wave at 440 Hz
tone_sine = Sine(440).to_audio_segment(duration=1000)

# Generate a 1-second square wave at 540 Hz
tone_square = Square(540).to_audio_segment(duration=1000)

# Generate a 1-second sawtooth wave at 640 Hz
tone_sawtooth = Sawtooth(640).to_audio_segment(duration=1000)

# Normalize and apply effects to each tone
tone_sine_normalized = tone_sine.apply_gain(-tone_sine.dBFS)
tone_square_normalized = tone_square.apply_gain(-tone_square.dBFS).fade_in(500).fade_out(500)
tone_sawtooth_normalized = tone_sawtooth.apply_gain(-tone_sawtooth.dBFS).invert_phase()

# Pan the tones to different sides
# PyDub's pan method: -1.0 is full left, 1.0 is full right.
tone_sine_pan = tone_sine_normalized.pan(-0.5)  # Pan left
tone_square_pan = tone_square_normalized.pan(0)  # Center
tone_sawtooth_pan = tone_sawtooth_normalized.pan(0.5)  # Pan right

# Combine the tones into a single track
combined_tones = tone_sine_pan.overlay(tone_square_pan).overlay(tone_sawtooth_pan)

# Save the combined audio to a file
combined_file_path = './tmp/combined_tones.mp3'
combined_tones.export(combined_file_path, format="mp3")

print(f"Combined multi-track MP3 file saved to '{combined_file_path}'")