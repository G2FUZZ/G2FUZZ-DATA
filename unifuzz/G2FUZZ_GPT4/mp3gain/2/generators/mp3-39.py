import numpy as np
import scipy.io.wavfile as wavfile
import os
from pydub import AudioSegment
from tempfile import TemporaryDirectory
import eyed3
import subprocess
import datetime

# Ensure the `./tmp/` directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate a stereo sine wave as an example of audio
def generate_stereo_sine_wave(freq_left, freq_right, sample_rate, duration):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    left_channel = np.sin(2 * np.pi * freq_left * t)
    right_channel = np.sin(2 * np.pi * freq_right * t)
    return np.vstack((left_channel, right_channel)).T

# Parameters for the stereo audio
freq_left = 440  # Frequency of the sine wave for the left channel (A4)
freq_right = 554.37  # Frequency of the sine wave for the right channel (C#5)
sample_rate = 44100  # Sample rate in Hz
duration = 5  # Duration in seconds

# Generate a stereo sine wave audio signal
audio = generate_stereo_sine_wave(freq_left, freq_right, sample_rate, duration)

# Normalize to 16-bit range for WAV format
audio_normalized = np.int16((audio / np.max(np.abs(audio))) * 32767)

# Use a temporary directory to first save as WAV
with TemporaryDirectory() as tmpdirname:
    wav_path = os.path.join(tmpdirname, 'temp.wav')
    mp3_path = './tmp/generated_audio.mp3'  # MP3 saved in ./tmp/
    
    # Write the stereo audio data as a WAV file
    wavfile.write(wav_path, sample_rate, audio_normalized)
    
    # Convert WAV to MP3 with VBR
    sound = AudioSegment.from_wav(wav_path)
    sound.export(mp3_path, format="mp3", parameters=["-q:a", "0"])  # '-q:a 0' enables VBR with the highest quality

    # Adding ReplayGain Information to the MP3 file
    mp3gain_path = '/usr/local/bin/mp3gain'  # Adjust this path as necessary
    try:
        subprocess.run([mp3gain_path, mp3_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error adding ReplayGain: {e}")
    except FileNotFoundError as e:
        print(f"mp3gain not found. Please ensure it is installed and the path is correct: {e}")

# Adding Encapsulated Data, Watermarking & Lyrics
audiofile = eyed3.load(mp3_path)
if audiofile.tag is None:
    audiofile.initTag()

audiofile.tag.artist = "Example Artist"
audiofile.tag.album = "Example Album"
# Convert datetime.date to eyed3.core.Date and assign
today = datetime.date.today()
audiofile.tag.recording_date = eyed3.core.Date(today.year, today.month, today.day)
audiofile.tag.title = "Stereo Sine Wave"
audiofile.tag.lyrics.set(u"Here are the lyrics of the song.")

# Specify the correct path to an image file for album art
image_path = './tmp/your_image.jpg'  # Adjust this path to your actual image file
try:
    with open(image_path, 'rb') as img_file:
        audiofile.tag.images.set(3, img_file.read(), 'image/jpeg')
except FileNotFoundError:
    print(f"Error: The specified image file was not found at {image_path}")

audiofile.tag.save()

print(f"Generated MP3 saved to: {mp3_path}")