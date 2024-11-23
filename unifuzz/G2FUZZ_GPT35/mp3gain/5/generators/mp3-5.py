import soundfile as sf
import numpy as np

# Create a mono channel mp3 file
mono_data = np.random.randn(44100)  # Generating random mono audio data
sf.write('./tmp/mono.mp3', mono_data, samplerate=44100)

# Create a stereo channel mp3 file
stereo_data = np.random.randn(44100, 2)  # Generating random stereo audio data
sf.write('./tmp/stereo.mp3', stereo_data, samplerate=44100)