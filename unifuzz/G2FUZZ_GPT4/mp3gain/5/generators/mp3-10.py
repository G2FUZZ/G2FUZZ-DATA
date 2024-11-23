import numpy as np
from pydub import AudioSegment
import os

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate a sine wave as an example audio signal
sample_rate = 44100  # Sample rate in Hz
duration = 5  # Duration in seconds
frequency = 440  # Frequency of the sine wave in Hz
amplitude = 4096  # Amplitude of the sine wave

t = np.linspace(0, duration, int(sample_rate * duration))
audio_signal = (np.sin(2 * np.pi * frequency * t) * amplitude).astype(np.int16)

# Create an AudioSegment from the raw audio data
audio_segment = AudioSegment(
    data=audio_signal.tobytes(), 
    sample_width=2,  # 2 bytes per sample, as we used int16
    frame_rate=sample_rate, 
    channels=1  # Mono
)

# Export the AudioSegment as an MP3 file
audio_segment.export("./tmp/example_streaming_capability.mp3", format="mp3")

print("MP3 file with streaming capability created at './tmp/example_streaming_capability.mp3'")