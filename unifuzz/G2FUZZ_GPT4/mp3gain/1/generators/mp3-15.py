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
        
        # Define filename
        filename = f'./tmp/sine_{frequency}Hz_{sample_rate}sample_rate_streaming.mp3'
        
        # Export the audio file with parameters that favor streaming
        # Note: While PyDub itself does not have specific streaming optimization parameters,
        # encoding with a constant bitrate (CBR) can facilitate smoother streaming.
        # Additional tweaks might involve using external libraries or tools for deeper control over MP3 encoding parameters.
        audio_segment.export(filename, format="mp3", bitrate="128k", parameters=["-write_xing", "0"])
        
        print(f"Generated {filename} with Streaming Support")