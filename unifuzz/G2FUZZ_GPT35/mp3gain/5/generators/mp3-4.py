import numpy as np
import soundfile as sf

# Create a random audio signal
duration = 5  # 5 seconds
sampling_rate = 44100  # Default CD quality
num_samples = duration * sampling_rate
audio_signal = np.random.uniform(low=-1, high=1, size=num_samples)

# Save the audio signal as an mp3 file
output_path = './tmp/random_audio.mp3'
sf.write(output_path, audio_signal, samplerate=sampling_rate, format='mp3')

print(f"MP3 file with sampling rate {sampling_rate} Hz saved at {output_path}")