import numpy as np
from scipy.io.wavfile import write
import os
from pydub import AudioSegment
from pydub.effects import normalize

# Ensure the tmp directory exists
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

def generate_sine_wave(freq, sample_rate, duration, volume=1.0, pan=0.0):
    """
    Generate a sine wave with a given frequency, sample rate, and duration.
    Volume adjustment and stereo panning are applied.
    """
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    note = np.sin(freq * t * 2 * np.pi)
    note *= volume
    # Normalize to 16-bit range and apply volume
    audio = note * (2**15 - 1) / np.max(np.abs(note))
    # Create stereo effect
    if pan < 0:
        left = audio * (1 + pan)
        right = audio
    else:
        left = audio
        right = audio * (1 - pan)
    stereo_audio = np.vstack((left, right)).T
    return stereo_audio.astype(np.int16)

def generate_chord(frequencies, sample_rate, duration, volume=1.0, pan=0.0):
    """
    Generate a chord by adding multiple sine waves, with volume and stereo panning.
    """
    chord = np.zeros((int(sample_rate * duration), 2))
    for freq in frequencies:
        chord += generate_sine_wave(freq, sample_rate, duration, volume, pan)
    # Normalize to prevent clipping
    chord = chord * (2**15 - 1) / np.max(np.abs(chord))
    return chord.astype(np.int16)

def generate_melody(chords, sample_rate, durations, volumes=None, pans=None):
    """
    Generate a melody by sequencing chords, with optional volume changes and stereo panning.
    """
    melody = np.array([], dtype=np.int16).reshape(0,2)
    if volumes is None:
        volumes = [1.0] * len(chords)
    if pans is None:
        pans = [0.0] * len(chords)
    for chord, duration, volume, pan in zip(chords, durations, volumes, pans):
        note = generate_chord(chord, sample_rate, duration, volume, pan)
        melody = np.vstack((melody, note))
    return melody

def save_as_mp3(audio, sample_rate, filename):
    """
    Save the generated audio (stereo) as an MP3 file, applying normalization for consistent volume.
    """
    wav_file = filename.replace('.mp3', '_temp.wav')
    write(wav_file, sample_rate, audio)
    sound = AudioSegment.from_wav(wav_file)
    sound = normalize(sound)
    sound.export(filename, format="mp3")
    os.remove(wav_file)

# Define parameters for a more complex melody
frequencies = [[440], [494], [523], [587], [659], [698], [784]]  # Notes from A4 to G5
durations = [0.4] * 7  # 0.4 seconds per note
volumes = [0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 0.8]  # Gradual volume increase
pans = [-0.5, -0.3, -0.1, 0, 0.1, 0.3, 0.5]  # Stereo panning from left to right
sample_rate = 44100  # 44.1 kHz

melody = generate_melody(frequencies, sample_rate, durations, volumes, pans)
filename = './tmp/complex_melody.mp3'
save_as_mp3(melody, sample_rate, filename)
print(f"Generated {filename}")

# Define parameters for a sequence of chords with fading effects
chord_frequencies = [[440, 554.37, 659.25], [523, 659.25, 783.99]]  # A Major and G Major chords
chord_durations = [2, 2]  # 2 seconds per chord
chord_volumes = [0.8, 1.0]  # Volume changes between chords
chord_pans = [0.0, 0.0]  # Center panning for simplicity
chord_melody = generate_melody(chord_frequencies, sample_rate, chord_durations, chord_volumes, chord_pans)
chord_filename = './tmp/complex_chords.mp3'
save_as_mp3(chord_melody, sample_rate, chord_filename)
print(f"Generated {chord_filename}")