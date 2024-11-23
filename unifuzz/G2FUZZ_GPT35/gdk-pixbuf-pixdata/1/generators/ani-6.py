import os

# Create a directory to save the 'ani' files
os.makedirs('./tmp/', exist_ok=True)

# Generate and save 'ani' files with metadata
metadata = {
    'author': 'John Doe',
    'creation_date': '2022-10-01',
    'description': 'Sample animation file'
}

for i in range(3):
    filename = f'./tmp/ani_file_{i}.ani'
    with open(filename, 'w') as file:
        file.write("# Metadata\n")
        for key, value in metadata.items():
            file.write(f"{key}: {value}\n")
        file.write("\n# Animation data\n")
        file.write("Frame 1: ...\n")
        file.write("Frame 2: ...\n")
        file.write("Frame 3: ...\n")

print("Generated 'ani' files with metadata successfully.")