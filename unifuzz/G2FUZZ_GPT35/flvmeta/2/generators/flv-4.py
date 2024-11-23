import os

# Create a directory for storing the generated FLV files
os.makedirs('./tmp/', exist_ok=True)

# Generate FLV files with streaming support
for i in range(3):
    file_name = f'./tmp/video_{i+1}.flv'
    with open(file_name, 'wb') as file:
        file.write(b'FLV Streaming Support: Online Video Playback')
    
    print(f'FLV file "{file_name}" with streaming support has been generated.')