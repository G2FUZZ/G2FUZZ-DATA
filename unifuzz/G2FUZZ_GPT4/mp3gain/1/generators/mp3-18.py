import numpy as np
import os
from pydub import AudioSegment

# Ensure the tmp directory exists
os.makedirs('./tmp', exist_ok=True)

# Define sample rates in kHz
sample_rates = [44100, 48000]

# Generate a sine wave for demonstration
duration_seconds = 5  # 5 seconds of audio
frequencies = [440, 880]  # Frequencies in Hz for A4 and A5 notes

for sample_rate in sample_rates:
    for frequency in frequencies:
        # Create a time array
        t = np.linspace(0, duration_seconds, int(sample_rate * duration_seconds), False)
        
        # Generate sine wave
        audio_signal = np.sin(2 * np.pi * frequency * t) * 32767  # 32767 to scale to int16 range
        
        # Convert to int16, the format expected by PyDub
        audio_signal = audio_signal.astype(np.int16)
        
        # Create an audio segment
        audio_segment = AudioSegment(audio_signal.tobytes(), frame_rate=sample_rate, sample_width=2, channels=1)
        
        # Perform Loudness Normalization
        target_loudness = -20.0  # Target loudness in dBFS
        change_in_loudness = target_loudness - audio_segment.dBFS
        normalized_audio_segment = audio_segment.apply_gain(change_in_loudness)
        
        # Define filename
        filename = f'./tmp/sine_{frequency}Hz_{sample_rate}sample_rate_normalized.mp3'
        
        # Export the audio file with loudness normalization
        normalized_audio_segment.export(filename, format="mp3")
        
        print(f"Generated {filename} with loudness normalization")