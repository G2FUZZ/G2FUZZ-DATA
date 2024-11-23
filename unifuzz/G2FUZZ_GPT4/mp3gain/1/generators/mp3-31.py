from pydub import AudioSegment
from pydub.generators import Sine
from pydub.effects import normalize
import os

# Ensure the tmp directory exists
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

def generate_tone(frequency, duration):
    """Generate a sine wave tone for a given frequency and duration."""
    tone = Sine(frequency).to_audio_segment(duration=duration)
    return normalize(tone)

def generate_chord(frequencies, duration):
    """Generate a chord from multiple frequencies."""
    chord = AudioSegment.silent(duration=0)
    for freq in frequencies:
        tone = generate_tone(freq, duration)
        chord = chord.overlay(tone)
    return chord

def generate_silence(duration):
    """Generate a segment of silence for a given duration."""
    return AudioSegment.silent(duration=duration)

# Frequencies for the notes in a C major and G major chord (in Hz)
c_major_freqs = [261.63, 329.63, 392]  # C, E, G
g_major_freqs = [196, 247.5, 392]  # G, B, D

# Generate chords and silence
c_major_chord = generate_chord(c_major_freqs, duration=2000)  # 2 seconds
g_major_chord = generate_chord(g_major_freqs, duration=2000)  # 2 seconds
silence = generate_silence(1000)  # 1 second

# Combine everything
sequence = c_major_chord + silence + g_major_chord

# Export the combined audio segment to an MP3 file
file_path = './tmp/chord_sequence.mp3'
sequence.export(file_path, format="mp3", bitrate="192k")

print(f"File has been saved to {file_path}")