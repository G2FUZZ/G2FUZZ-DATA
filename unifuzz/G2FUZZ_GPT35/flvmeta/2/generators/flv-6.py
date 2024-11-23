import os

# Create a directory to store the generated files
os.makedirs('./tmp/', exist_ok=True)

# Generate FLV files with the specified features
features = "Compatibility: FLV files are widely supported by various media players and web browsers."

for i in range(3):
    with open(f'./tmp/file_{i}.flv', 'w') as file:
        file.write(features)