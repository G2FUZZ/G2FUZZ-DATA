import numpy as np
from scipy.io.wavfile import write
from pydub import AudioSegment
import os

def generate_sine_wave(frequency, duration, sample_rate=44100, amplitude=0.5):
    """
    Generates a sine wave for a given frequency and duration.
    """
    time = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    audio = np.sin(2 * np.pi * frequency * time) * amplitude
    audio = (audio * 32767).astype(np.int16)  # Convert to 16-bit PCM format
    return audio

def create_chord(frequencies, duration, sample_rate=44100, amplitude=0.5):
    """
    Generates a chord by combining multiple sine waves.
    """
    chord = np.zeros(int(sample_rate * duration), dtype=np.int16)
    for frequency in frequencies:
        wave = generate_sine_wave(frequency, duration, sample_rate, amplitude / len(frequencies))
        chord += wave
    return chord

def create_melody(notes, duration, sample_rate=44100, amplitude=0.5):
    """
    Generates a sequence of notes to create a simple melody.
    """
    melody = np.array([], dtype=np.int16)
    for note in notes:
        wave = generate_sine_wave(note, duration, sample_rate, amplitude)
        melody = np.concatenate((melody, wave))
    return melody

# Ensure the tmp directory exists
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Example: Generating a chord and a simple melody
sample_rate = 44100  # Sample rate in Hz
chord_frequencies = [440, 550, 660]  # Frequencies in Hz for a chord
melody_notes = [440, 494, 554, 587, 659, 740, 831, 880]  # Frequencies in Hz for a melody
duration = 1  # Duration in seconds for each note/chord

# Generate a chord
chord = create_chord(chord_frequencies, duration, sample_rate)
# Generate a melody
melody = create_melody(melody_notes, duration, sample_rate)

# Combine chord and melody
combined_audio = np.concatenate((chord, melody))
combined_audio = combined_audio.astype(np.int16)

# Save the combined audio as a temporary WAV file
temp_wave_file = os.path.join(output_dir, "complex_audio.wav")
write(temp_wave_file, sample_rate, combined_audio)

# Convert the WAV file to MP3 using pydub, adding fade-in and fade-out effects
audio_segment = AudioSegment.from_wav(temp_wave_file)
audio_segment = audio_segment.fade_in(2000).fade_out(3000)  # Fade-in for 2s, Fade-out for 3s
mp3_file = os.path.join(output_dir, "complex_audio.mp3")
audio_segment.export(mp3_file, format="mp3", bitrate="128k")

# Clean up the temporary WAV file
os.remove(temp_wave_file)

print(f"Complex MP3 file saved to: {mp3_file}")