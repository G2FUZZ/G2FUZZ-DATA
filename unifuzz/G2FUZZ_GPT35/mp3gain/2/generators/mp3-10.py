import os

# Create a directory to store the generated mp3 files
os.makedirs('./tmp/', exist_ok=True)

# Generate mp3 files with different layers
layers = ['Layer I', 'Layer II', 'Layer III']

for layer in layers:
    filename = f'./tmp/example_{layer.replace(" ", "_")}.mp3'
    with open(filename, 'w') as file:
        file.write(f'File: {filename}\n')
        file.write(f'Layer support: {layer}\n')
    print(f'Generated {filename}')