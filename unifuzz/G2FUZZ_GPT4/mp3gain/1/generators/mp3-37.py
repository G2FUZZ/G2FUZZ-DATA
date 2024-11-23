import numpy as np
import pydub
from pydub.generators import Sine
import os
from scipy.signal import butter, lfilter

# Ensure the tmp directory exists
os.makedirs('./tmp', exist_ok=True)

# Define necessary functions for filtering
def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

# Define a function to generate a sine wave with frequency modulation using bandpass filtering
def generate_fm_sine_wave(frequency=440, modulation_frequency=5, modulation_index=2, duration_seconds=5, volume=-20.0, sample_rate=44100):
    # Time array
    t = np.linspace(0, duration_seconds, int(sample_rate * duration_seconds))
    # Modulated frequency
    fm_wave = np.sin(2 * np.pi * (frequency + modulation_index * np.sin(2 * np.pi * modulation_frequency * t)) * t)
    # Bandpass filter (example usage, modify as needed for actual filtering)
    # fm_wave_filtered = butter_bandpass_filter(fm_wave, 20, 2000, sample_rate)
    # Convert to audio segment
    fm_wave = (fm_wave * np.iinfo(np.int16).max).astype(np.int16)
    fm_audio = pydub.AudioSegment(fm_wave.tobytes(), frame_rate=sample_rate, sample_width=2, channels=1)
    return fm_audio

# Define a function to generate a sequence of tones with stereo effect
def generate_tone_sequence(frequencies=[440, 554, 660], durations=[1, 1, 1], volume=-20.0, sample_rate=44100):
    sequence_audio = pydub.AudioSegment.empty()
    for freq, dur in zip(frequencies, durations):
        sine_wave_left = Sine(freq).to_audio_segment(duration=dur * 1000, volume=volume)
        sine_wave_right = Sine(freq + 10).to_audio_segment(duration=dur * 1000, volume=volume)  # Slight frequency shift for stereo effect
        stereo_wave = pydub.AudioSegment.from_mono_audiosegments(sine_wave_left, sine_wave_right)
        sequence_audio += stereo_wave
    return sequence_audio

# Extended function to generate MP3 with more features using bandpass filtering and stereo effects
def generate_mp3_complex_features():
    # FM Sine Wave with Bandpass Filter (placeholder for filtering, adjust as needed)
    fm_audio = generate_fm_sine_wave()
    fm_audio.export('./tmp/fm_sine_wave.mp3', format='mp3', bitrate='192k', tags={"artist": "Algorithm", "title": "FM Sine Wave"})
    
    # Tone Sequence with Stereo Effect
    tone_sequence_audio = generate_tone_sequence()
    tone_sequence_audio.export('./tmp/tone_sequence_stereo.mp3', format='mp3', bitrate='192k', tags={"artist": "Algorithm", "title": "Tone Sequence Stereo"})
    
    # Stereo with FM Sine Wave (For demonstrating a complex stereo effect)
    stereo_fm_audio = pydub.AudioSegment.from_mono_audiosegments(fm_audio, fm_audio.invert_phase())
    stereo_fm_audio.export('./tmp/stereo_fm_sine_wave.mp3', format='mp3', bitrate='192k', tags={"artist": "Algorithm", "title": "Stereo FM Sine Wave"})

# Generate MP3 files with complex features
generate_mp3_complex_features()