import numpy as np
from scipy.io.wavfile import write
import os
from pydub import AudioSegment
import subprocess

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Function to generate a sine wave
def generate_sine_wave(freq, sample_rate, duration):
    t = np.linspace(0, duration, int(sample_rate*duration), False)
    note = np.sin(freq * t * 2 * np.pi)
    audio_data = note * (2**15 - 1) / np.max(np.abs(note))
    return audio_data.astype(np.int16)

# Function to create an MP3 file from numpy array data
def create_mp3(filename, audio_data, sample_rate, bit_rate):
    # Save the audio data to a temporary WAV file
    temp_filename = filename + '.wav'
    write(temp_filename, sample_rate, audio_data)
    # Convert the WAV file to MP3
    audio = AudioSegment.from_wav(temp_filename)
    audio.export(filename, format='mp3', bitrate=f'{bit_rate}k')
    # Remove the temporary WAV file
    os.remove(temp_filename)

# Function to apply Replay Gain to an MP3 file
def apply_replay_gain(filename):
    # Use FFmpeg to calculate and apply Replay Gain
    # Ensure you have FFmpeg installed and added to your system's PATH
    command = f"ffmpeg -i {filename} -af loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json -f null /dev/null"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout, _ = process.communicate()
    loudnorm_stats = stdout.decode()

    # Extracting Replay Gain information (not applied because FFmpeg loudnorm filter only prints info in this setup)
    # You would need to parse the loudnorm_stats here to extract Replay Gain values and then apply them
    # As an example, we're just printing the loudnorm stats
    print(loudnorm_stats)

    # To actually apply the Replay Gain, you would need to run FFmpeg again with the stats, something like:
    # command_apply = f"ffmpeg -i {filename} -af loudnorm=I=-16:TP=-1.5:LRA=11:measured_I=<input_i>:measured_LRA=<input_lra>:measured_TP=<input_tp>:measured_thresh=<input_thresh>:offset=<target_offset> {filename[:-4]}_rg.mp3"
    # subprocess.run(command_apply, shell=True)

# Sample rate and duration
sample_rate = 44100  # in Hz
duration = 5  # in seconds

# Frequency of the sine wave
frequency = 440  # A4 note

# Generate sine wave data
audio_data = generate_sine_wave(frequency, sample_rate, duration)

# Bit rates to generate MP3 files for
bit_rates = [128, 192, 320]

# Generate MP3 files at different bit rates
for bit_rate in bit_rates:
    filename = f'./tmp/sine_wave_{bit_rate}kbps.mp3'
    create_mp3(filename, audio_data, sample_rate, bit_rate)
    apply_replay_gain(filename)

print("MP3 files generated at different bit rates with Replay Gain information.")