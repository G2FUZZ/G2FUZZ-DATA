import os
import random

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Additional complex features for FLV files
def generate_flv_file(filename):
    duration = random.randint(60, 600)  # Random duration between 1 to 10 minutes
    resolution = f'{random.randint(480, 1080)}p'  # Random resolution between 480p to 1080p
    codec = random.choice(['H.264', 'VP9', 'AV1'])  # Random codec type

    with open(filename, 'wb') as file:
        file.write(f'FLV File\nDuration: {duration} seconds\nResolution: {resolution}\nCodec: {codec}'.encode())

# Generate FLV files with additional complex features
for i in range(3):
    filename = f'./tmp/file_{i}.flv'
    generate_flv_file(filename)

print('FLV files with additional complex features generated successfully.')