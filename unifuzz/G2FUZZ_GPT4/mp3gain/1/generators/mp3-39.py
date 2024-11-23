import os
import numpy as np
from scipy.io.wavfile import write
from scipy.signal import butter, lfilter
from pydub import AudioSegment

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

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

# Parameters for the audio signal
sample_rate = 44100  # Sample rate in Hz
duration = 5  # Duration in seconds

# Two frequencies for stereo effect
frequency_left = 440  # Frequency of the left channel sine wave in Hz
frequency_right = 554  # Frequency of the right channel sine wave in Hz

# Generate a sine wave for each channel with given parameters
t = np.linspace(0, duration, int(sample_rate * duration), False)
audio_signal_left = np.sin(2 * np.pi * frequency_left * t)
audio_signal_right = np.sin(2 * np.pi * frequency_right * t)

# Apply bandpass filter (dummy settings for demonstration)
filtered_left = butter_bandpass_filter(audio_signal_left, 20, 8000, sample_rate)
filtered_right = butter_bandpass_filter(audio_signal_right, 20, 8000, sample_rate)

# Convert the audio signals to 16-bit integers
audio_signal_left_int16 = np.int16(filtered_left * 32767)
audio_signal_right_int16 = np.int16(filtered_right * 32767)

# Save each channel as a separate WAV file
wav_file_path_left = './tmp/generated_audio_left.wav'
wav_file_path_right = './tmp/generated_audio_right.wav'
write(wav_file_path_left, sample_rate, audio_signal_left_int16)
write(wav_file_path_right, sample_rate, audio_signal_right_int16)

# Combine the WAV files into a single stereo MP3
audio_left = AudioSegment.from_wav(wav_file_path_left)
audio_right = AudioSegment.from_wav(wav_file_path_right)
stereo_audio = AudioSegment.from_mono_audiosegments(audio_left, audio_right)

# Save the stereo audio to an MP3 file with different bit rates
bit_rates = [128, 192, 256, 320]
for bit_rate in bit_rates:
    mp3_file_path = f'./tmp/generated_stereo_audio_{bit_rate}kbps.mp3'
    stereo_audio.export(mp3_file_path, format="mp3", bitrate=f"{bit_rate}k")

# Remove the temporary WAV files
os.remove(wav_file_path_left)
os.remove(wav_file_path_right)