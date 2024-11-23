import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate 'ani' files with optimization techniques
for i in range(5):
    file_name = f'./tmp/ani_file_{i}.ani'
    with open(file_name, 'w') as f:
        f.write("Optimization: 'ani' files may have optimization techniques to enhance performance.\n")

print("Files generated successfully!")