import numpy as np
import soundfile as sf
import lameenc

# Create a dummy audio signal
sample_rate = 44100  # Sample rate of 44.1 kHz for CD quality audio
duration = 5  # Duration of the audio signal in seconds

num_samples = int(sample_rate * duration)
audio_signal = np.random.uniform(low=-1, high=1, size=num_samples)

# Save the audio signal as an MP3 file with specific file features
file_path = './tmp/generated_audio.mp3'

encoder = lameenc.Encoder()
encoder.set_bit_rate(320)  # Set a higher quality bitrate of 320 kbps
encoder.set_in_sample_rate(sample_rate)
encoder.set_channels(1)  # Mono audio
encoder.set_quality(2)  # Set quality to 2 (0=low, 9=high)

chunk_size = 1152
num_chunks = len(audio_signal) // chunk_size

with open(file_path, 'wb') as f:
    for i in range(num_chunks):
        chunk = audio_signal[i * chunk_size : (i + 1) * chunk_size]
        encoded_data = encoder.encode(chunk)
        f.write(encoded_data)
    
    # Handle the remaining samples
    if len(audio_signal) % chunk_size != 0:
        chunk = audio_signal[num_chunks * chunk_size :]
        encoded_data = encoder.encode(chunk)
        f.write(encoded_data)
    
    encoded_data = encoder.flush()
    f.write(encoded_data)