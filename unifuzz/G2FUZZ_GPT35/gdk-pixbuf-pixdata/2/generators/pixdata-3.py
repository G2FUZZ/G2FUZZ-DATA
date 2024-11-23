import numpy as np
import os

# Generate random data for features
num_files = 5
num_features = 100
num_samples = 1000
data = np.random.rand(num_samples, num_features)

# Create tmp directory if it doesn't exist
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Save generated data into pixdata files with compression
for i in range(num_files):
    filename = f'./tmp/pixdata_{i}.npz'
    np.savez_compressed(filename, data=data)

print(f'{num_files} pixdata files generated and saved into ./tmp/')