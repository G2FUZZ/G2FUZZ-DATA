import os

# Create a directory for saving generated files
os.makedirs('./tmp/', exist_ok=True)

# Define the content of the 'ras' files
ras_content = """\
Features:
- External dependencies: 'ras' files may require external libraries or software to open and view the image data, especially if specialized compression or encoding methods are used.
"""

# Generate 'ras' files with the specified features
for i in range(3):
    with open(f'./tmp/file_{i}.ras', 'w') as file:
        file.write(ras_content)