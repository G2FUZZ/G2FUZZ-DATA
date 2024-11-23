import numpy as np
import scipy.io.wavfile as wavfile
import os
from pydub import AudioSegment
from tempfile import TemporaryDirectory
import eyed3
import subprocess

# Ensure the `./tmp/` directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate a sine wave as an example of audio
def generate_sine_wave(freq, sample_rate, duration):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    return np.sin(2 * np.pi * freq * t)

# Function to adjust sampling rate based on audio content
def adjust_sampling_rate(audio, original_rate, target_rates):
    # Example heuristic: Use lower sample rate for simpler audio
    # This is a placeholder for actual logic to analyze and decide on the sample rate
    # For simplicity, switching between two rates based on max frequency component
    fft_result = np.fft.rfft(audio)
    max_freq = np.argmax(np.abs(fft_result))
    
    # Assuming if max frequency component is below a threshold, use lower sample rate
    if max_freq < len(fft_result) / 4:
        new_rate = target_rates[0]  # Lower quality for less complex audio
    else:
        new_rate = target_rates[1]  # Higher quality for more complex audio
    
    # Resample the audio to the new rate
    resampled_audio = np.interp(
        np.linspace(0, len(audio), int(len(audio) * new_rate / original_rate)),
        np.arange(len(audio)),
        audio
    )
    return new_rate, resampled_audio

# Parameters for the audio
freq = 440  # Frequency of the sine wave (A4)
sample_rate = 44100  # Sample rate in Hz
duration = 5  # Duration in seconds

# Generate a sine wave audio signal
audio = generate_sine_wave(freq, sample_rate, duration)

# Apply scalable sampling rate feature
# Example: switching between two sample rates based on audio content
new_sample_rate, audio_adjusted = adjust_sampling_rate(audio, sample_rate, [22050, 44100])

# Normalize to 16-bit range for WAV format
audio_normalized = np.int16((audio_adjusted / audio_adjusted.max()) * 32767)

# Use a temporary directory to first save as WAV
with TemporaryDirectory() as tmpdirname:
    wav_path = os.path.join(tmpdirname, 'temp.wav')
    mp3_path = './tmp/generated_audio.mp3'  # MP3 saved in ./tmp/
    
    # Write the audio data as a WAV file
    wavfile.write(wav_path, new_sample_rate, audio_normalized)
    
    # Convert WAV to MP3
    sound = AudioSegment.from_wav(wav_path)
    sound.export(mp3_path, format="mp3", bitrate="192k")

    # Adding ReplayGain Information to the MP3 file
    mp3gain_path = '/usr/local/bin/mp3gain'  # Adjust this path as necessary
    try:
        subprocess.run([mp3gain_path, mp3_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error adding ReplayGain: {e}")
    except FileNotFoundError as e:
        print(f"mp3gain not found. Please ensure it is installed and the path is correct: {e}")

# Adding Encapsulated Data & Watermarking (e.g., album art)
audiofile = eyed3.load(mp3_path)
if audiofile.tag is None:
    audiofile.initTag()

# Specify the correct path to an image file for album art
image_path = './tmp/your_image.jpg'  # Adjust this path to your actual image file
try:
    with open(image_path, 'rb') as img_file:
        audiofile.tag.images.set(3, img_file.read(), 'image/jpeg')
except FileNotFoundError:
    print(f"Error: The specified image file was not found at {image_path}")

audiofile.tag.save()

print(f"Generated MP3 saved to: {mp3_path}")