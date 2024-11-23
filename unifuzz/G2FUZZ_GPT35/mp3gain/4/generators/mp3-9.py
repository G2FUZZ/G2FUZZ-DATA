# Import necessary libraries
import os
import numpy as np
import soundfile as sf

# Create a directory to store the generated mp3 files if it doesn't exist
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Generate a sample audio file with some random data
sample_rate = 44100
duration = 10  # in seconds
num_samples = sample_rate * duration
data = np.random.uniform(-1, 1, num_samples)

# Save the generated audio data as an mp3 file
file_path = os.path.join(output_dir, 'editable.mp3')
sf.write(file_path, data, sample_rate)

print(f"Generated editable mp3 file: {file_path}")