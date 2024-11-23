import os
import random

# Create a directory to save the generated files
os.makedirs('./tmp/', exist_ok=True)

# Generate 5 'mp3' files with variable bit rates
for i in range(1, 6):
    filename = f'./tmp/audio_{i}.mp3'
    vbr = random.randint(0, 9)  # Simulating a random variable bit rate from 0 to 9
    print(f'Generating {filename} with VBR: {vbr}')

    # Simulating the generation of an 'mp3' file with variable bit rate
    with open(filename, 'wb') as file:
        file.write(b'Simulated audio data')

print('Files generated successfully!')