import numpy as np
import os
from moviepy.editor import AudioFileClip
from scipy.io.wavfile import write as wav_write  # Import the wav write function

# Ensure the tmp directory exists
os.makedirs('./tmp', exist_ok=True)

# Generate a synthetic sine wave for demonstration
def generate_sine_wave(frequency=440, duration=5, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate*duration), False)
    note = np.sin(frequency * t * 2 * np.pi)
    # Normalize to 16-bit range
    audio = note * (2**15 - 1) / np.max(np.abs(note))
    return audio.astype(np.int16)

# Modified function to accept ffmpeg_params and pass it to write_audiofile
def create_audio_file(filename, audio_samples, sample_rate=44100, codec='libmp3lame', ffmpeg_params=None):
    if ffmpeg_params is None:
        ffmpeg_params = []
    # Temporary filename for the WAV file
    temp_wav_filename = './tmp/temp_audio.wav'
    # Save the numpy array to a WAV file
    wav_write(temp_wav_filename, sample_rate, audio_samples)
    # Create an audio clip from the WAV file
    audio_clip = AudioFileClip(temp_wav_filename)
    # Write the audio clip to an mp4 file with the specified codec and ffmpeg_params
    audio_clip.write_audiofile(filename, codec=codec, ffmpeg_params=ffmpeg_params)
    # Optionally, remove the temporary WAV file after use (uncomment the line below if desired)
    # os.remove(temp_wav_filename)

# Generate a sine wave
sample_rate = 44100
audio_samples = generate_sine_wave(sample_rate=sample_rate)

# Save the audio with lossy compression
lossy_filename = './tmp/lossy_audio.mp4'
create_audio_file(lossy_filename, audio_samples, sample_rate, codec='aac')

# Save the audio with lossless compression
lossless_filename = './tmp/lossless_audio.mp4'
create_audio_file(lossless_filename, audio_samples, sample_rate, codec='aac', ffmpeg_params=['-q:a', '0'])

print("Files have been generated and saved to ./tmp/")