import os

# Create a directory to store the generated files
os.makedirs('./tmp/', exist_ok=True)

# Define the sample rates to be used for generating the MP3 files
sample_rates = [8000, 16000, 32000, 48000]

for i, sample_rate in enumerate(sample_rates):
    # Generate a simple MP3 file with the specified sample rate
    filename = f'./tmp/sample_{i}.mp3'
    with open(filename, 'wb') as f:
        f.write(b'Generated MP3 file with sample rate: ' + str(sample_rate).encode())

print('MP3 files generated successfully.')