from pydub import AudioSegment
from pydub.generators import Sine
import numpy as np
import os
from scipy.signal import butter, lfilter

def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y

def apply_custom_eq(audio_segment, eq_settings):
    """
    Apply a simple form of equalization using a low-pass filter.
    This is a placeholder for a more complex EQ implementation.
    """
    # Convert PyDub audio_segment to numpy array
    samples = np.array(audio_segment.get_array_of_samples())
    sample_rate = audio_segment.frame_rate
    
    # Apply low-pass filter based on the first eq_setting for demonstration
    cutoff = eq_settings[0][0][1]  # Use high_freq of the first band as cutoff
    filtered_samples = butter_lowpass_filter(samples, cutoff, sample_rate)
    
    # Convert back to PyDub AudioSegment
    filtered_audio = audio_segment._spawn(filtered_samples.astype(np.int16).tobytes())
    
    return filtered_audio

# Ensure the tmp directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Generate a 440 Hz sine wave (A4 note) for 5 seconds
frequency = 440  # Frequency in Hz
duration = 5000  # Duration in milliseconds
volume = -20.0  # Volume in dB

# Generate sine wave
tone = Sine(frequency, sample_rate=44100).to_audio_segment(duration=duration, volume=volume)

# Example EQ settings: Boost bass and treble, reduce mids
# Format: [((low_freq, high_freq), gain_db), ...]
eq_settings = [
    ((20, 60), 5),    # Boost lower bass
    ((250, 2000), -5), # Reduce mid-range
    ((4000, 6000), 3)  # Enhance presence
]

# Apply EQ settings to the tone
tone_with_eq = apply_custom_eq(tone, eq_settings)

# Save the generated tone with EQ as an MP3 file
output_path = os.path.join(output_dir, 'generated_tone_with_eq.mp3')
tone_with_eq.export(output_path, format="mp3", bitrate="128k")

print(f"MP3 file with Customizable EQ Settings saved to {output_path}")