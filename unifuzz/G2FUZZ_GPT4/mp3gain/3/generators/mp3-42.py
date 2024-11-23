import os
from pydub import AudioSegment
from pydub.generators import Sine
from pydub.effects import normalize, speedup, invert_phase
import lameenc

def generate_complex_structure_mp3(filename, duration_ms=500, base_freq=440):
    # Generate a sequence of chords with silence between them
    chords = []
    # Define a chord as a combination of frequencies (e.g., a major chord: base, major third, perfect fifth)
    chord_intervals = [1, 5/4, 3/2]  # Major chord intervals
    silence_duration_ms = 250

    for multiplier in chord_intervals:
        # Generate each note of the chord
        freq = base_freq * multiplier
        note = Sine(freq).to_audio_segment(duration=duration_ms)
        note = normalize(note)
        chords.append(note)

    # Combine notes to form a chord
    chord = AudioSegment.silent(duration=0)
    for note in chords:
        chord = chord.overlay(note)

    # Create a sequence of chords with silence in between
    sequence = AudioSegment.silent(duration=0)
    for _ in range(3):  # Repeat the chord 3 times
        sequence += chord + AudioSegment.silent(duration=silence_duration_ms)

    # Apply effects
    # Speed up the sequence
    sequence = speedup(sequence, playback_speed=1.1)
    # Invert phase of the sequence to demonstrate an effect (could be used for stereo effects)
    sequence = invert_phase(sequence)

    # Convert to raw audio data
    raw_audio_data = sequence.raw_data

    # Encoding settings for MP3
    encoder = lameenc.Encoder()
    encoder.set_bit_rate(192)
    encoder.set_in_sample_rate(sequence.frame_rate)
    encoder.set_channels(2)  # Assuming stereo
    encoder.set_quality(2)  # High quality

    # Encode to MP3
    mp3_data = encoder.encode(raw_audio_data)
    mp3_data += encoder.flush()

    # Save to file
    with open(filename, 'wb') as f:
        f.write(mp3_data)

    print(f"Generated complex structure MP3: {filename}")

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate and save MP3 file with a complex structure
filename = './tmp/complex_structure_chord_sequence.mp3'
generate_complex_structure_mp3(filename)