import os

# Create a directory for storing the generated FLV files
os.makedirs('./tmp/', exist_ok=True)

# Generate FLV files with complex file structures
for i in range(4):
    file_name = f'./tmp/video_{i+1}.flv'
    with open(file_name, 'wb') as file:
        # Video metadata
        file.write(b'FLV Header: Video Codec - H.264, Audio Codec - AAC\n')
        
        # Video data
        file.write(b'Video Data: H.264 encoded video frames\n')
        
        # Audio data
        file.write(b'Audio Data: AAC encoded audio samples\n')
        
        # Cue points for navigation
        file.write(b'Cue Points: { "time": 10, "label": "Chapter 1" }, { "time": 30, "label": "Chapter 2" }\n')
    
    print(f'FLV file "{file_name}" with complex file structures has been generated.')