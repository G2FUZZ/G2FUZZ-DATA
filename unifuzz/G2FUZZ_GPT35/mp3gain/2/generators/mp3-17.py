import os
import random

# Create a directory to save the generated files
os.makedirs('./tmp/', exist_ok=True)

def generate_mp3_file(filename):
    vbr = random.randint(0, 9)  # Simulating a random variable bit rate from 0 to 9
    frame_length = random.choice([1152, 576, 192])  # Simulating variable frame length options
    print(f'Generating {filename} with VBR: {vbr} and frame length: {frame_length}')

    # Simulating the generation of an 'mp3' file with variable bit rate and frame length
    with open(filename, 'wb') as file:
        file.write(b'Simulated audio data')

# Generate 5 'mp3' files with variable bit rates and frame lengths
for i in range(1, 6):
    filename = f'./tmp/audio_{i}.mp3'
    generate_mp3_file(filename)

print('Files generated successfully!')