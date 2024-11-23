import numpy as np
from scipy.io.wavfile import write
import os
from pydub import AudioSegment

# Ensure the tmp directory exists
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Function to generate a sine wave with volume control
def generate_sine_wave(freq, sample_rate, duration, volume=1.0, pan=0.0):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    note = np.sin(freq * t * 2 * np.pi) * volume
    # Normalize to 16-bit range, considering the volume
    audio = note * (2**15 - 1) / np.max(np.abs(note))
    audio = audio.astype(np.int16)
    # Pan the note left or right
    if pan != 0.0:
        left = audio * min(1.0 - pan, 1.0)
        right = audio * min(1.0 + pan, 1.0)
        audio = np.vstack((left, right)).T
    else:
        audio = np.vstack((audio, audio)).T  # Make it stereo without panning
    return audio

# Function to generate chords
def generate_chord(frequencies, sample_rate, duration, volume=1.0, pan=0.0):
    chord = np.zeros((int(sample_rate * duration), 2)) # Initialize a stereo signal
    for freq in frequencies:
        note = generate_sine_wave(freq, sample_rate, duration, volume, pan)
        chord[:, 0] += note[:, 0]  # Left channel
        chord[:, 1] += note[:, 1]  # Right channel
    # Normalize to prevent clipping
    chord = chord * (2**15 - 1) / np.max(np.abs(chord))
    return chord.astype(np.int16)

# Function to apply fade in and fade out
def apply_fade(audio, sample_rate, fade_in_duration, fade_out_duration):
    num_samples = audio.shape[0]
    fade_in_samples = int(fade_in_duration * sample_rate)
    fade_out_samples = int(fade_out_duration * sample_rate)

    # Apply fade in
    for i in range(fade_in_samples):
        audio[i, :] = audio[i, :] * (i / fade_in_samples)
    
    # Apply fade out
    for i in range(fade_out_samples):
        audio[-i-1, :] = audio[-i-1, :] * (i / fade_out_samples)
    
    return audio

# Function to save the audio as an MP3 file
def save_as_mp3(audio, sample_rate, filename):
    # Convert the NumPy array to bytes
    audio_bytes = audio.tobytes()
    # Create a PyDub audio segment
    sound = AudioSegment(audio_bytes, sample_width=2, frame_rate=sample_rate, channels=2)
    # Export as MP3
    sound.export(filename, format="mp3")

sample_rate = 44100  # 44.1 kHz

# Define parameters for tracks
tracks = []

# Chord progression: C major, F major, G major, C major
chords = [
    ([261.63, 329.63, 392.00], 1.0, 0.0),  # C major
    ([174.61, 261.63, 349.23], 1.0, -0.2),  # F major
    ([196.00, 293.66, 392.00], 1.0, 0.2),   # G major
    ([261.63, 329.63, 392.00], 1.0, 0.0)   # C major again
]

duration_chord = 1.5  # seconds per chord
for freqs, volume, pan in chords:
    chord = generate_chord(freqs, sample_rate, duration_chord, volume=volume, pan=pan)
    chord = apply_fade(chord, sample_rate, 0.1, 0.1)  # Apply fade in and out
    if len(tracks) == 0:
        tracks = chord
    else:
        tracks = np.vstack((tracks, chord))

# Save the composition as an MP3
filename = './tmp/complex_composition_stereo.mp3'
save_as_mp3(tracks, sample_rate, filename)
print(f"Generated {filename}")