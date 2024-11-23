import os

# Create a directory to save the generated FLV files
os.makedirs('./tmp/', exist_ok=True)

# Generate FLV files with metadata
metadata = {
    'video_duration': '2 hours',
    'dimensions': '1920x1080',
    'frame_rate': '30 fps'
}

for i in range(3):  # Generate 3 FLV files
    file_name = f'./tmp/file_{i}.flv'
    with open(file_name, 'wb') as file:
        # Write metadata information to the FLV file
        file.write(f'Metadata: {metadata}'.encode())
        
print('FLV files with metadata generated successfully.')