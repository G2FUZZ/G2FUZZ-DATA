import os
import numpy as np
from pydub import AudioSegment

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Function to generate a multi-frequency sine wave tone
def generate_multi_tone(frequencies, duration_ms=1000, volume=0.5, sample_rate=44100):
    duration = duration_ms / 1000
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = np.zeros(int(sample_rate * duration))
    # Add waves for each frequency
    for frequency in frequencies:
        wave += np.sin(frequency * t * 2 * np.pi)
    wave /= len(frequencies)  # Normalize
    # Normalize to 16-bit range and apply volume
    audio = wave * (2**15 - 1) * volume
    # Ensure data type is int16
    audio = audio.astype(np.int16)
    return audio

# Generate tones with multiple frequencies for a richer sound
frequencies_left = [440, 554.37, 659.25]  # A4, C#5/Eb5, E5
frequencies_right = [660, 880, 1760]  # E5, A5, A6
left_channel = generate_multi_tone(frequencies=frequencies_left, volume=0.5)
right_channel = generate_multi_tone(frequencies=frequencies_right, volume=0.5)

# Create stereo audio segment
stereo_audio = AudioSegment.from_mono_audiosegments(
    AudioSegment(left_channel.tobytes(), sample_width=2, frame_rate=44100, channels=1),
    AudioSegment(right_channel.tobytes(), sample_width=2, frame_rate=44100, channels=1)
)

# Function to apply a simple echo effect
def apply_echo(audio_segment, delay_ms=500, decay_factor=0.5):
    # Calculate the delay in terms of PyDub's milliseconds
    delay = delay_ms
    # Create a silent segment for the delay period
    silence = AudioSegment.silent(duration=delay)
    # Create the initial echo by appending the silence to the original audio
    echo = silence + audio_segment
    # Lower the volume of the echo
    echo = echo - (decay_factor * 100)  # PyDub's volume control is in dB
    # Overlay the original audio with the echo
    combined = audio_segment.overlay(echo)
    return combined

# Apply an echo effect
echo_audio = apply_echo(stereo_audio, delay_ms=500, decay_factor=0.5)

# Export stereo audio with echo effect at different quality levels
echo_audio.export("./tmp/high_quality.mp3", format="mp3", bitrate="320k")  # High quality
echo_audio.export("./tmp/medium_quality.mp3", format="mp3", bitrate="192k")  # Medium quality
echo_audio.export("./tmp/low_quality.mp3", format="mp3", bitrate="128k")  # Low quality

print("MP3 files with echo effect generated in './tmp/' directory at various quality levels.")