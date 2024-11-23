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

def generate_tone_with_crossfade(frequency, duration, volume, eq_settings, crossfade_duration):
    # Generate sine wave
    tone = Sine(frequency, sample_rate=44100).to_audio_segment(duration=duration, volume=volume)
    
    # Apply EQ settings to the tone
    tone_with_eq = apply_custom_eq(tone, eq_settings)
    
    # Apply crossfade. Crossfade the beginning and end of the tone with itself
    crossfaded_tone = tone_with_eq.append(tone_with_eq, crossfade=crossfade_duration).fade_in(crossfade_duration).fade_out(crossfade_duration)
    
    return crossfaded_tone

# Ensure the tmp directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Frequency, duration, and volume for the tone
frequency = 440  # Frequency in Hz
duration = 5000  # Duration in milliseconds
volume = -20.0  # Volume in dB
crossfade_duration = 1000  # Crossfade duration in milliseconds

# Example EQ settings
eq_settings = [
    ((20, 60), 5),    # Boost lower bass
    ((250, 2000), -5), # Reduce mid-range
    ((4000, 6000), 3)  # Enhance presence
]

# Generate tone with EQ and crossfade
tone_with_eq_and_crossfade = generate_tone_with_crossfade(frequency, duration, volume, eq_settings, crossfade_duration)

# Save the generated tone with EQ and crossfade as an MP3 file
output_path = os.path.join(output_dir, 'generated_tone_with_eq_and_crossfade.mp3')
tone_with_eq_and_crossfade.export(output_path, format="mp3", bitrate="128k")

print(f"MP3 file with Customizable EQ Settings and Crossfade Support saved to {output_path}")