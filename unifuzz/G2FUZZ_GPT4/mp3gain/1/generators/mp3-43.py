import os
from pydub import AudioSegment
from pydub.generators import Sine
from mutagen.id3 import ID3, TIT2, TPE1, TALB, TCON, TRCK, TYER, APIC, COMM
from mutagen.mp3 import MP3
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

def apply_custom_eq(audio_segment):
    samples = np.array(audio_segment.get_array_of_samples(), dtype=np.float64)
    sample_rate = audio_segment.frame_rate
    # Example EQ settings for demonstration
    eq_settings = [((300, 600), 2), ((1000, 2000), -3), ((3000, 5000), 4)]
    filtered_samples = np.zeros_like(samples)
    
    for eq_setting in eq_settings:
        lowcut, highcut = eq_setting[0]
        gain = eq_setting[1]
        band_filtered = butter_bandpass_filter(samples, lowcut, highcut, sample_rate) * gain
        filtered_samples += band_filtered

    filtered_samples = np.clip(filtered_samples, -32768, 32767)
    filtered_audio = audio_segment._spawn(filtered_samples.astype(np.int16).tobytes())
    return filtered_audio

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate a sine wave tone for 5 seconds, 440 Hz
tone = Sine(440).to_audio_segment(duration=5000)

# Apply custom EQ to the tone
tone_with_eq = apply_custom_eq(tone)

# Save the generated tone to a file
file_path = './tmp/generated_tone_with_eq.mp3'
tone_with_eq.export(file_path, format="mp3")

# Add metadata to the mp3 file
audio = MP3(file_path, ID3=ID3)

# Add various metadata
audio.tags.add(TIT2(encoding=3, text='Generated Tone with EQ'))
audio.tags.add(TPE1(encoding=3, text='Python Script'))
audio.tags.add(TALB(encoding=3, text='Generated Sounds'))
audio.tags.add(TCON(encoding=3, text='Synth'))
audio.tags.add(TRCK(encoding=3, text='1'))
audio.tags.add(TYER(encoding=3, text='2023'))

# Optional: Add an album cover
# with open('path/to/cover.jpg', 'rb') as albumart:
#     audio.tags.add(APIC(encoding=3, mime='image/jpeg', type=3, desc=u'Cover', data=albumart.read()))

# Optional: Add a comment
audio.tags.add(COMM(encoding=3, lang=u'eng', desc='desc', text='This is a generated MP3 file with EQ'))

audio.save()

print(f"Generated MP3 with EQ and metadata saved to {file_path}")