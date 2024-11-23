import numpy as np
from pydub import AudioSegment
from pydub.generators import Sine
import os

# Ensure the tmp directory exists
os.makedirs('./tmp/complex_structures/', exist_ok=True)

# Function to generate a sine wave tone with specified frequency, duration, and volume
def generate_tone(frequency, duration_ms, volume_db=-20):
    tone = Sine(frequency).to_audio_segment(duration=duration_ms).apply_gain(volume_db)
    return tone

# Generate multiple tones
tone1 = generate_tone(440, 1000)  # A4
tone2 = generate_tone(523.25, 1000)  # C5
tone3 = generate_tone(659.25, 1000)  # E5

# Combine tones sequentially to create a melody
melody = tone1 + tone2 + tone3

# Save the melody to a file
melody_file_path = './tmp/complex_structures/melody_tone.mp3'
melody.export(melody_file_path, format="mp3", tags={'artist': 'PyDub Orchestra', 'album': 'Tone Melodies', 'comments': 'A simple melody'})

# Create a stereo track with different tones in the left and right channels
left_channel = tone1.overlay(tone2)  # Combine tone1 and tone2 for the left channel
right_channel = tone3  # Use tone3 for the right channel

# Merge into a stereo track
stereo_track = AudioSegment.from_mono_audiosegments(left_channel, right_channel)

# Save the stereo track
stereo_file_path = './tmp/complex_structures/stereo_tone.mp3'
stereo_track.export(stereo_file_path, format="mp3", tags={'artist': 'PyDub SoundLab', 'album': 'Stereo Experiments', 'comments': 'A stereo track with different tones'})

# Generate a "complex structure" by creating a tone that increases in frequency over time
def generate_sweep_tone(start_freq, end_freq, duration_ms, volume_db=-20):
    step = (end_freq - start_freq) / duration_ms
    sweep_tone = AudioSegment.silent(duration=duration_ms)
    for t in range(duration_ms):
        freq = start_freq + step * t
        tone = Sine(freq).to_audio_segment(duration=1).apply_gain(volume_db)
        sweep_tone = sweep_tone.overlay(tone, position=t)
    return sweep_tone

sweep_tone = generate_sweep_tone(440, 880, 5000)  # Sweep from A4 to A5 over 5 seconds

# Save the sweep tone
sweep_file_path = './tmp/complex_structures/sweep_tone.mp3'
sweep_tone.export(sweep_file_path, format="mp3", tags={'artist': 'PyDub SoundLab', 'album': 'Frequency Sweeps', 'comments': 'A frequency sweep from A4 to A5'})

print("Melody, stereo track, and sweep tone MP3 files with custom metadata saved to './tmp/complex_structures/'")