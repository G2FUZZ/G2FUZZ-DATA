import numpy as np
import os
from pydub import AudioSegment
from pydub.generators import Sine
from pydub.effects import normalize

# Function to generate a stereo sine wave with panning and volume control
def generate_stereo_sine_wave(freq, duration_ms, volume=1.0, pan=0.0):
    # Generate the sine wave
    tone = Sine(freq).to_audio_segment(duration=duration_ms).apply_gain(volume)
    
    # Convert to stereo and apply panning
    tone_stereo = tone.set_channels(2)
    # Corrected: PyDub's pan takes values from -1.0 to 1.0
    tone_stereo = tone_stereo.pan(pan)
    
    return tone_stereo

# Function to apply fade in and fade out
def apply_fade(audio_segment, fade_in_duration_ms, fade_out_duration_ms):
    return audio_segment.fade_in(fade_in_duration_ms).fade_out(fade_out_duration_ms)

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate a 1-second (1000 ms) stereo sine wave at 440 Hz with panning and volume control
tone_stereo = generate_stereo_sine_wave(440, 1000, volume=0.8, pan=0.5)  # Panned to the right

# Apply fade in and fade out
tone_stereo_faded = apply_fade(tone_stereo, 100, 100)  # 100 ms fade in and fade out

# Save the generated sine wave to a file
file_path = './tmp/stereo_tone.mp3'
tone_stereo_faded.export(file_path, format="mp3")

print(f"Stereo, faded sine wave saved to '{file_path}'")