import os
import random

# Create a directory to store the generated 'pgx' files
os.makedirs('./tmp/', exist_ok=True)

# Generate 'pgx' files with advanced features
for i in range(5):
    filename = f'./tmp/file_{i}.pgx'
    
    # Simulate different image resolutions
    resolution = random.choice(['1920x1080', '1280x720', '3840x2160'])
    
    # Simulate metadata
    metadata = {
        'author': 'John Doe',
        'creation_date': '2022-08-15',
        'location': 'New York City'
    }
    
    with open(filename, 'w') as file:
        file.write(f"Resolution: {resolution}\n")
        file.write("Metadata:\n")
        for key, value in metadata.items():
            file.write(f"  {key}: {value}\n")
        file.write("\n")
        file.write("Text Overlay: This is a sample text overlay for additional information.")
        
print("Generated 'pgx' files with advanced features successfully.")