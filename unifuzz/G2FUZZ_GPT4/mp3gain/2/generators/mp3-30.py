import numpy as np
import scipy.io.wavfile as wavfile
import os
from pydub import AudioSegment
from tempfile import TemporaryDirectory

# Ensure the `./tmp/` directory exists
os.makedirs('./tmp/', exist_ok=True)

def generate_sine_wave(freq, sample_rate, duration):
    """
    Generate a sine wave for a given frequency.
    """
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    return np.sin(2 * np.pi * freq * t)

def generate_chord(freqs, sample_rate, duration):
    """
    Generate a chord by combining sine waves of different frequencies.
    """
    waves = [generate_sine_wave(freq, sample_rate, duration) for freq in freqs]
    chord = np.sum(waves, axis=0) / len(freqs)  # Normalize the sum of waves
    return chord

# Parameters for the audio
sample_rate = 44100  # Sample rate in Hz
duration = 2  # Duration in seconds for each chord

# Define a chord progression (in Hz)
chord_progression = [
    [440, 554.37, 659.25],  # A major: A, C#, E
    [392, 493.88, 587.33],  # G major: G, B, D
    [349.23, 440, 523.25],  # F major: F, A, C
    [293.66, 369.99, 440]   # D minor: D, F, A
]

# Use a temporary directory to first save as WAV, then convert to MP3
with TemporaryDirectory() as tmpdirname:
    wav_paths = []
    for i, chord_freqs in enumerate(chord_progression):
        chord = generate_chord(chord_freqs, sample_rate, duration)
        audio_normalized = np.int16((chord / chord.max()) * 32767)
        
        # Save each chord as a separate WAV file initially
        wav_path = os.path.join(tmpdirname, f'chord_{i}.wav')
        wavfile.write(wav_path, sample_rate, audio_normalized)
        wav_paths.append(wav_path)
    
    # Combine all the WAV files into a single audio segment
    combined = AudioSegment.empty()
    for wav_path in wav_paths:
        sound = AudioSegment.from_wav(wav_path)
        combined += sound
    
    # Final MP3 path
    mp3_path = './tmp/chord_progression.mp3'
    
    # Export the combined audio to MP3 with quality settings
    bitrate = "192k"
    encoding_quality = 2
    combined.export(mp3_path, format="mp3", bitrate=bitrate, parameters=["-q:a", str(encoding_quality)])

print(f"Generated MP3 saved to: {mp3_path}")