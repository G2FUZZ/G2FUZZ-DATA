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
    fft_result = np.fft.rfft(audio)
    max_freq = np.argmax(np.abs(fft_result))
    
    if max_freq < len(fft_result) / 4:
        new_rate = target_rates[0]
    else:
        new_rate = target_rates[1]
    
    resampled_audio = np.interp(
        np.linspace(0, len(audio), int(len(audio) * new_rate / original_rate)),
        np.arange(len(audio)),
        audio
    )
    return new_rate, resampled_audio

freq = 440
sample_rate = 44100
duration = 5

audio = generate_sine_wave(freq, sample_rate, duration)
new_sample_rate, audio_adjusted = adjust_sampling_rate(audio, sample_rate, [22050, 44100])
audio_normalized = np.int16((audio_adjusted / audio_adjusted.max()) * 32767)

with TemporaryDirectory() as tmpdirname:
    wav_path = os.path.join(tmpdirname, 'temp.wav')
    mp3_path = './tmp/generated_audio.mp3'
    
    wavfile.write(wav_path, new_sample_rate, audio_normalized)
    sound = AudioSegment.from_wav(wav_path)
    sound.export(mp3_path, format="mp3", bitrate="192k")

    mp3gain_path = '/usr/local/bin/mp3gain'
    try:
        subprocess.run([mp3gain_path, mp3_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error adding ReplayGain: {e}")
    except FileNotFoundError as e:
        print(f"mp3gain not found. Please ensure it is installed and the path is correct: {e}")

audiofile = eyed3.load(mp3_path)
if audiofile.tag is None:
    audiofile.initTag()

image_path = './tmp/your_image.jpg'
try:
    with open(image_path, 'rb') as img_file:
        audiofile.tag.images.set(3, img_file.read(), 'image/jpeg')
except FileNotFoundError:
    print(f"Error: The specified image file was not found at {image_path}")

# Correctly add a user-defined text frame (TXXX)
audiofile.tag.user_text_frames.set("ISO/IEC Standardization", "MP3, formally known as ISO/IEC 11172-3 MPEG-1 Audio Layer III and ISO/IEC 13818-3 MPEG-2 Audio Layer III, is standardized by the International Organization for Standardization (ISO) and the International Electrotechnical Commission (IEC), ensuring consistent implementation across platforms and devices.")
audiofile.tag.save()

print(f"Generated MP3 saved to: {mp3_path}")