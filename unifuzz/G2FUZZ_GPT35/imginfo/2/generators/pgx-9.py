import os

# Create a directory to store the generated 'pgx' files
os.makedirs('./tmp/', exist_ok=True)

# Generate 'pgx' files with annotations
for i in range(3):
    filename = f'./tmp/file_{i}.pgx'
    with open(filename, 'w') as file:
        file.write("Annotations: Some 'pgx' files may support annotations or text overlays for adding additional information to the image.")

print("Generated 'pgx' files with annotations successfully.")