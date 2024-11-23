import os
from pydub import AudioSegment
from pydub.generators import Sine
import numpy as np
from scipy.signal import butter, lfilter

# Define necessary functions
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

def apply_custom_eq(audio_segment, eq_settings):
    samples = np.array(audio_segment.get_array_of_samples(), dtype=np.float64)
    sample_rate = audio_segment.frame_rate
    filtered_samples = np.zeros_like(samples)
    
    for eq_setting in eq_settings:
        lowcut, highcut = eq_setting[0]
        gain = eq_setting[1]
        band_filtered = butter_bandpass_filter(samples, lowcut, highcut, sample_rate) * gain
        filtered_samples += band_filtered

    filtered_samples = np.clip(filtered_samples, -32768, 32767)
    filtered_audio = audio_segment._spawn(filtered_samples.astype(np.int16).tobytes())
    return filtered_audio

def generate_stereo_tone(frequency_left, frequency_right, duration, volume, eq_settings, crossfade_duration):
    tone_left = Sine(frequency_left, sample_rate=44100).to_audio_segment(duration=duration, volume=volume)
    tone_right = Sine(frequency_right, sample_rate=44100).to_audio_segment(duration=duration, volume=volume)
    tone_left_with_eq = apply_custom_eq(tone_left, eq_settings)
    tone_right_with_eq = apply_custom_eq(tone_right, eq_settings)
    stereo_tone_with_eq = AudioSegment.from_mono_audiosegments(tone_left_with_eq, tone_right_with_eq)
    crossfaded_stereo_tone = stereo_tone_with_eq.append(stereo_tone_with_eq, crossfade=crossfade_duration).fade_in(crossfade_duration).fade_out(crossfade_duration)
    return crossfaded_stereo_tone

# Ensure the tmp directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)  # This avoids raising an error if the directory already exists

# Define parameters for the tone generation and EQ settings
frequency_left = 440
frequency_right = 554
duration = 5000
volume = -20.0
crossfade_duration = 1000
eq_settings = [((20, 60), 2), ((250, 2000), -3), ((4000, 6000), 4), ((8000, 12000), 5)]

# Generate the stereo tone with EQ and crossfade
stereo_tone_with_eq_and_crossfade = generate_stereo_tone(frequency_left, frequency_right, duration, volume, eq_settings, crossfade_duration)

# Save the generated tone
output_path = os.path.join(output_dir, 'generated_stereo_tone_with_eq_and_crossfade.mp3')
stereo_tone_with_eq_and_crossfade.export(output_path, format="mp3", bitrate="128k")

print(f"MP3 file with Customizable EQ Settings and Crossfade Support saved to {output_path}")