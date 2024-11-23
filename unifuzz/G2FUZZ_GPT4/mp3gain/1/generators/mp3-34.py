import numpy as np
import pydub
from pydub.generators import Sine
import os

# Ensure the tmp directory exists
os.makedirs('./tmp', exist_ok=True)

# Define a function to generate a sine wave with frequency modulation
def generate_fm_sine_wave(frequency=440, modulation_frequency=5, modulation_index=2, duration_seconds=5, volume=-20.0, sample_rate=44100):
    # Time array
    t = np.linspace(0, duration_seconds, int(sample_rate * duration_seconds))
    # Modulated frequency
    fm_wave = np.sin(2 * np.pi * (frequency + modulation_index * np.sin(2 * np.pi * modulation_frequency * t)) * t)
    # Convert to audio segment
    fm_wave = (fm_wave * np.iinfo(np.int16).max).astype(np.int16)
    fm_audio = pydub.AudioSegment(fm_wave.tobytes(), frame_rate=sample_rate, sample_width=2, channels=1)
    return fm_audio

# Define a function to generate a sequence of tones
def generate_tone_sequence(frequencies=[440, 554, 660], durations=[1, 1, 1], volume=-20.0, sample_rate=44100):
    sequence_audio = pydub.AudioSegment.empty()
    for freq, dur in zip(frequencies, durations):
        sine_wave = Sine(freq).to_audio_segment(duration=dur * 1000, volume=volume)
        sequence_audio += sine_wave
    return sequence_audio

# Extended function to generate MP3 with more features
def generate_mp3_complex_features():
    # FM Sine Wave
    fm_audio = generate_fm_sine_wave()
    fm_audio.export('./tmp/fm_sine_wave.mp3', format='mp3', bitrate='192k', tags={"artist": "Algorithm", "title": "FM Sine Wave"})
    
    # Tone Sequence
    tone_sequence_audio = generate_tone_sequence()
    tone_sequence_audio.export('./tmp/tone_sequence.mp3', format='mp3', bitrate='192k', tags={"artist": "Algorithm", "title": "Tone Sequence"})
    
    # Stereo with FM Sine Wave (For demonstrating a complex stereo effect)
    stereo_fm_audio = pydub.AudioSegment.from_mono_audiosegments(fm_audio, fm_audio.invert_phase())
    stereo_fm_audio.export('./tmp/stereo_fm_sine_wave.mp3', format='mp3', bitrate='192k', tags={"artist": "Algorithm", "title": "Stereo FM Sine Wave"})

# Generate MP3 files with complex features
generate_mp3_complex_features()