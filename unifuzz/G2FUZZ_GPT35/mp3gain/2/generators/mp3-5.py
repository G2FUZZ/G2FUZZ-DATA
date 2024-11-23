import numpy as np
import soundfile as sf

# Create a stereo MP3 file
stereo_data = np.random.uniform(low=-1, high=1, size=(44100, 2))  # 2 channels (stereo), 44100 samples
sf.write('./tmp/stereo_file.mp3', stereo_data, 44100, format='mp3')

# Create a mono MP3 file
mono_data = np.random.uniform(low=-1, high=1, size=(44100, 1))  # 1 channel (mono), 44100 samples
sf.write('./tmp/mono_file.mp3', mono_data, 44100, format='mp3')