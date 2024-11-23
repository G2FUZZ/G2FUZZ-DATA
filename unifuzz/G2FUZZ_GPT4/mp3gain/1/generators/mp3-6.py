import numpy as np
import pydub
from pydub.generators import Sine
import os

# Ensure the tmp directory exists
os.makedirs('./tmp', exist_ok=True)

# Define a function to generate a sine wave and save it as an MP3 in different stereo modes
def generate_mp3_stereo_modes(frequency=440, duration_seconds=5, volume=-20.0, sample_rate=44100):
    # Generate a mono sine wave
    sine_wave = Sine(frequency).to_audio_segment(duration=duration_seconds * 1000, volume=volume)

    # Stereo
    stereo_audio = sine_wave.set_channels(2)
    stereo_audio.export('./tmp/stereo_mode.mp3', format='mp3', bitrate='192k')

    # Joint Stereo (not directly supported by PyDub, but we'll simulate it by creating a stereo file with slightly altered channels)
    joint_stereo_audio = pydub.AudioSegment.from_mono_audiosegments(sine_wave, sine_wave.invert_phase())
    joint_stereo_audio.export('./tmp/joint_stereo_mode.mp3', format='mp3', bitrate='192k')

    # Dual Channel (similar to stereo but with the same audio in both channels)
    dual_channel_audio = pydub.AudioSegment.from_mono_audiosegments(sine_wave, sine_wave)
    dual_channel_audio.export('./tmp/dual_channel_mode.mp3', format='mp3', bitrate='192k')

    # Mono
    mono_audio = sine_wave.set_channels(1)
    mono_audio.export('./tmp/mono_mode.mp3', format='mp3', bitrate='192k')

# Generate MP3 files with different stereo modes
generate_mp3_stereo_modes()