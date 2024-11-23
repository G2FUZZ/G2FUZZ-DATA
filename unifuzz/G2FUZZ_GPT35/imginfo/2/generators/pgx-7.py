import os

# Create a directory to store the generated 'pgx' files
os.makedirs('./tmp/', exist_ok=True)

# Generate 'pgx' files with transparency settings
for i in range(3):
    with open(f'./tmp/file_{i}.pgx', 'w') as file:
        file.write("# Transparency: 'pgx' files may support transparency settings to enable alpha blending and image overlays.")

print("Files generated successfully.")