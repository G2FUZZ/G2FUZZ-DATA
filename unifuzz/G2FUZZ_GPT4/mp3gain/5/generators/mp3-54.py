import os
from pydub import AudioSegment
from pydub.generators import Sine, Square, Sawtooth, WhiteNoise

# Ensure the './tmp/' directory exists
os.makedirs('./tmp/', exist_ok=True)

# Function to generate a wave audio segment with different wave forms
def generate_wave(frequency, duration_in_ms, volume, wave_type="sine"):
    if wave_type == "sine":
        wave = Sine(frequency)
    elif wave_type == "square":
        wave = Square(frequency)
    elif wave_type == "sawtooth":
        wave = Sawtooth(frequency)
    else:
        raise ValueError(f"Unsupported wave type: {wave_type}")
    return wave.to_audio_segment(duration=duration_in_ms, volume=volume)

# Function to create a chord by overlaying multiple frequencies
def generate_chord(frequencies, duration_in_ms, volume, wave_type="sine"):
    chord = AudioSegment.silent(duration=duration_in_ms)
    for freq in frequencies:
        wave = generate_wave(freq, duration_in_ms, volume, wave_type)
        chord = chord.overlay(wave)
    return chord

# Function to create a section of music by repeating a pattern
def create_section(pattern, repeat, fade_duration=1000):
    section = pattern * repeat
    return section.fade_in(fade_duration).fade_out(fade_duration)

# Intro: A simple melody using sine waves
intro_chord_frequencies = [[440, 554.37, 659.25], [659.25, 554.37, 440]]  # A major chord then reverse
intro_pattern = AudioSegment.silent(duration=0)
for chord_freqs in intro_chord_frequencies:
    intro_pattern += generate_chord(chord_freqs, 2000, -20.0, "sine")
intro = create_section(intro_pattern, 1)

# Verse: A rhythmic pattern using square waves
verse_chord_frequencies = [440, 659.25, 554.37]  # Single notes for simplicity
verse_pattern = AudioSegment.silent(duration=0)
for freq in verse_chord_frequencies:
    verse_pattern += generate_wave(freq, 500, -15.0, "square")
verse = create_section(verse_pattern, 4)

# Chorus: A fuller sound with sawtooth waves and background noise
chorus_chord_frequencies = [[440, 554.37, 659.25], [659.25, 554.37, 440]]  # A major chord and reverse
chorus_pattern = AudioSegment.silent(duration=0)
for chord_freqs in chorus_chord_frequencies:
    chord = generate_chord(chord_freqs, 2000, -10.0, "sawtooth")
    noise = WhiteNoise().to_audio_segment(duration=2000, volume=-30.0)
    chord_with_noise = chord.overlay(noise)
    chorus_pattern += chord_with_noise
chorus = create_section(chorus_pattern, 2)

# Combine all sections
song = intro + verse + chorus

# Export the generated composition
file_path = './tmp/complex_composition.mp3'
song.export(file_path, format="mp3", bitrate="192k")

print(f"Generated mp3 file with a complex structure at {file_path}")