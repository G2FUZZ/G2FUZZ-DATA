import numpy as np
from pydub import AudioSegment
from pydub.generators import Sine
import os

# Ensure the tmp directory exists
os.makedirs('./tmp/complex_structures/', exist_ok=True)

# Function to generate a sine wave tone with specified frequency, duration, volume, and pan
def generate_tone(frequency, duration_ms, volume_db=-20, pan=0.0):
    # Generate the tone
    tone = Sine(frequency).to_audio_segment(duration=duration_ms).apply_gain(volume_db)
    # Apply panning if necessary
    if pan != 0.0:
        tone = tone.pan(pan)
    return tone

# Generate tones with panning for a stereo effect
tone1 = generate_tone(440, 1000, pan=-0.5)  # A4, panned left
tone2 = generate_tone(523.25, 1000, pan=0)  # C5, centered
tone3 = generate_tone(659.25, 1000, pan=0.5)  # E5, panned right

# Combine tones sequentially to create a melody
melody = tone1.append(tone2, crossfade=0).append(tone3, crossfade=0)

# Apply fade in and fade out to the melody
melody = melody.fade_in(200).fade_out(200)

# Save the melody to a file
melody_file_path = './tmp/complex_structures/melody_tone.mp3'
melody.export(melody_file_path, format="mp3", tags={'artist': 'PyDub Orchestra', 'album': 'Tone Melodies', 'comments': 'A simple melody with stereo panning'})

# Generate a "complex structure" by creating a tone that increases in frequency over time with stereo panning
def generate_sweep_tone(start_freq, end_freq, duration_ms, volume_db=-20):
    step = (end_freq - start_freq) / duration_ms
    sweep_tone_left = AudioSegment.silent(duration=duration_ms)
    sweep_tone_right = AudioSegment.silent(duration=duration_ms)
    for t in range(duration_ms):
        freq = start_freq + step * t
        left_tone = Sine(freq).to_audio_segment(duration=1).apply_gain(volume_db - 5)  # Slightly quieter in the left channel
        right_tone = Sine(freq).to_audio_segment(duration=1).apply_gain(volume_db + 5)  # Slightly louder in the right channel
        sweep_tone_left = sweep_tone_left.overlay(left_tone, position=t)
        sweep_tone_right = sweep_tone_right.overlay(right_tone, position=t)
    # Combine the left and right tones for a stereo effect
    sweep_tone = AudioSegment.from_mono_audiosegments(sweep_tone_left, sweep_tone_right)
    return sweep_tone

sweep_tone = generate_sweep_tone(440, 880, 5000)  # Sweep from A4 to A5 over 5 seconds

# Save the sweep tone
sweep_file_path = './tmp/complex_structures/sweep_tone.mp3'
sweep_tone.export(sweep_file_path, format="mp3", tags={'artist': 'PyDub SoundLab', 'album': 'Frequency Sweeps', 'comments': 'A stereo frequency sweep from A4 to A5'})

print("Melody, and sweep tone MP3 files with custom metadata and stereo effects saved to './tmp/complex_structures/'")