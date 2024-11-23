import numpy as np
from scipy.io.wavfile import write
import os
from pydub import AudioSegment

# Ensure the tmp directory exists
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Function to generate a sine wave
def generate_sine_wave(freq, sample_rate, duration):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    note = np.sin(freq * t * 2 * np.pi)
    # Normalize to 16-bit range
    audio = note * (2**15 - 1) / np.max(np.abs(note))
    return audio.astype(np.int16)

# Function to generate a chord by adding multiple sine waves
def generate_chord(frequencies, sample_rate, duration):
    chord = np.zeros(int(sample_rate * duration))
    for freq in frequencies:
        chord += generate_sine_wave(freq, sample_rate, duration)
    # Normalize to prevent clipping
    chord = chord * (2**15 - 1) / np.max(np.abs(chord))
    return chord.astype(np.int16)

# Function to generate a simple melody by sequencing notes or chords
def generate_melody(chords, sample_rate, durations):
    melody = np.array([], dtype=np.int16)
    for chord, duration in zip(chords, durations):
        note = generate_chord(chord, sample_rate, duration)
        melody = np.concatenate((melody, note))
    return melody

# Function to save the audio as an MP3 file
def save_as_mp3(audio, sample_rate, filename):
    # Save the generated audio as a WAV file first
    wav_file = filename.replace('.mp3', '.wav')
    write(wav_file, sample_rate, audio)
    # Convert the WAV to MP3
    sound = AudioSegment.from_wav(wav_file)
    sound.export(filename, format="mp3")
    # Remove the WAV file
    os.remove(wav_file)

# Define parameters for a simple melody
frequencies = [[440], [494], [523], [587], [659], [698], [784]]  # Notes from A4 to G5
durations = [0.4] * 7  # 0.4 seconds per note
sample_rate = 44100  # 44.1 kHz

# Generate and save a simple melody
melody = generate_melody(frequencies, sample_rate, durations)
filename = './tmp/simple_melody.mp3'
save_as_mp3(melody, sample_rate, filename)
print(f"Generated {filename}")

# Define parameters for a chord
chord_frequencies = [[440, 554.37, 659.25]]  # A major chord: A4, C#5, and E5
chord_duration = [2]  # 2 seconds
chord_melody = generate_melody(chord_frequencies, sample_rate, chord_duration)
chord_filename = './tmp/a_major_chord.mp3'
save_as_mp3(chord_melody, sample_rate, chord_filename)
print(f"Generated {chord_filename}")