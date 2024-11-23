import os
import numpy as np
from pydub import AudioSegment

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Function to generate a multi-frequency sine wave tone with stereo and pan control
def generate_multi_tone(frequencies, duration_ms=1000, volume=0.5, sample_rate=44100, pan=0.0):
    duration = duration_ms / 1000
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = np.zeros(int(sample_rate * duration))
    # Add waves for each frequency
    for frequency in frequencies:
        wave += np.sin(frequency * t * 2 * np.pi)
    wave /= len(frequencies)  # Normalize
    # Normalize to 16-bit range and apply volume
    audio = wave * (2**15 - 1) * volume
    audio = audio.astype(np.int16)
    # Pan the note left or right
    if pan != 0.0:
        left = audio * min(1.0 - pan, 1.0)
        right = audio * min(1.0 + pan, 1.0)
        audio = np.vstack((left, right)).T
    else:
        audio = np.vstack((audio, audio)).T  # Make it stereo without panning
    return audio

# Generate tones with multiple frequencies for a richer sound
frequencies_left = [440, 554.37, 659.25]  # A4, C#5/Eb5, E5
frequencies_right = [660, 880, 1760]  # E5, A5, A6
left_channel = generate_multi_tone(frequencies=frequencies_left, volume=0.5, pan=-0.2)
right_channel = generate_multi_tone(frequencies=frequencies_right, volume=0.5, pan=0.2)

# Combine the left and right channels
combined_stereo = np.vstack((left_channel, right_channel)).T  # Correct stacking for stereo

# Function to apply a simple echo effect (modified for stereo signals)
def apply_echo(audio, sample_rate=44100, delay_ms=500, decay_factor=0.5):
    delay_samples = int(sample_rate * (delay_ms / 1000))
    echo_signal = np.zeros_like(audio)
    echo_signal[delay_samples:] = audio[:-delay_samples] * decay_factor
    # Combine the original signal with the echo
    combined = audio + echo_signal
    return combined

# Apply an echo effect
echo_audio = apply_echo(combined_stereo, sample_rate=44100, delay_ms=500, decay_factor=0.5)

# Convert the NumPy array to bytes and create a PyDub audio segment for export
echo_audio_segment = AudioSegment(echo_audio.tobytes(), sample_width=2, frame_rate=44100, channels=2)

# Export stereo audio with echo effect at different quality levels
echo_audio_segment.export("./tmp/high_quality.mp3", format="mp3", bitrate="320k")  # High quality
echo_audio_segment.export("./tmp/medium_quality.mp3", format="mp3", bitrate="192k")  # Medium quality
echo_audio_segment.export("./tmp/low_quality.mp3", format="mp3", bitrate="128k")  # Low quality

print("MP3 files with echo effect generated in './tmp/' directory at various quality levels.")