import numpy as np
from scipy.io.wavfile import write
import os
from pydub import AudioSegment

# Ensure the tmp directory exists
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Function to generate a sine wave with volume control
def generate_sine_wave(freq, sample_rate, duration, volume=1.0):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    note = np.sin(freq * t * 2 * np.pi) * volume
    # Normalize to 16-bit range, considering the volume
    audio = note * (2**15 - 1) / np.max(np.abs(note))
    return audio.astype(np.int16)

# Function to generate a multi-track composition
def generate_composition(tracks, sample_rate):
    composition_length = max([len(track) for track in tracks])  # Find the longest track
    composition = np.zeros(composition_length)
    for track in tracks:
        composition[0:len(track)] += track  # Mix the tracks
    # Normalize to prevent clipping
    composition = composition * (2**15 - 1) / np.max(np.abs(composition))
    return composition.astype(np.int16)

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

sample_rate = 44100  # 44.1 kHz

# Define parameters for tracks
tracks = []
# Track 1: Melody
frequencies_melody = [440, 494, 523, 587, 659, 698, 784]  # Notes from A4 to G5
duration_melody = 0.4  # seconds per note
for freq in frequencies_melody:
    tracks.append(generate_sine_wave(freq, sample_rate, duration_melody, volume=0.8))

# Track 2: Bass line
frequencies_bass = [220, 220, 220, 220, 220, 220, 220]  # A constant bass line of A3
duration_bass = 0.8  # Longer notes for the bass line
for freq in frequencies_bass:
    tracks.append(generate_sine_wave(freq, sample_rate, duration_bass, volume=0.6))

# Mix tracks and generate the composition
composition = generate_composition(tracks, sample_rate)

# Save the composition as an MP3
filename = './tmp/complex_composition.mp3'
save_as_mp3(composition, sample_rate, filename)
print(f"Generated {filename}")