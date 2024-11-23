import os

# Create a directory to store the ani files
os.makedirs('./tmp/', exist_ok=True)

# Generate and save the ani files
ani_content = "Compatibility: 'ani' files are primarily used in Windows systems and may have limitations in cross-platform compatibility."
for i in range(3):
    with open(f'./tmp/file_{i}.ani', 'w') as f:
        f.write(ani_content)