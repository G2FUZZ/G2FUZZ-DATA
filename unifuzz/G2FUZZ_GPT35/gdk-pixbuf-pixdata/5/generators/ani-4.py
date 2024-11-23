import os

# Create a directory to store the generated 'ani' files
os.makedirs('./tmp/', exist_ok=True)

# Generate 'ani' files with interactive elements
for i in range(3):
    file_name = f'./tmp/ani_file_{i}.ani'
    with open(file_name, 'w') as f:
        f.write(f'Interactive ' + str(i) + ': Clickable areas or triggers')

print('Generated interactive "ani" files successfully.')