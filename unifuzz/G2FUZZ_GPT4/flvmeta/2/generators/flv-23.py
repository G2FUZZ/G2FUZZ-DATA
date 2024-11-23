from moviepy.editor import AudioFileClip
import numpy as np
import os
from scipy.io.wavfile import write

# Ensure the tmp directory exists
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Function to generate a sine wave tone
def generate_sine_wave(frequency, duration, sample_rate=44100):
    t = np.linspace(0, duration, int(duration * sample_rate), False)
    tone = np.sin(frequency * t * 2 * np.pi)
    return (tone * 0.5 * (2**15 - 1)).astype(np.int16)

# Generate a 1-second sine wave at 440Hz
sample_rate = 44100
tone = generate_sine_wave(440, 1, sample_rate)  # Corrected the typo here

# Save the tone as a temporary WAV file (will be used to create FLV files)
wav_filename = './tmp/temp_tone.wav'
write(wav_filename, sample_rate, tone)  # Use scipy's write function to save the WAV file properly

# Load the WAV file as an audio clip
audio_clip = AudioFileClip(wav_filename)

# Export the audio clip as FLV with MP3 codec
mp3_flv_filename = './tmp/audio_mp3.flv'
audio_clip.write_audiofile(mp3_flv_filename, codec='libmp3lame')

# Export the audio clip as FLV with AAC codec
aac_flv_filename = './tmp/audio_aac.flv'
audio_clip.write_audiofile(aac_flv_filename, codec='aac')

# Extract audio from the FLV file and save it as MP3
extracted_audio_filename = './tmp/extracted_audio.mp3'
audio_clip.write_audiofile(extracted_audio_filename)

# Clean up the temporary WAV file
os.remove(wav_filename)

print("FLV files with audio have been saved to ./tmp/")
print("Extracted audio has also been saved as MP3 in ./tmp/")