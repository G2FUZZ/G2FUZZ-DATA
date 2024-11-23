import os

# Create a directory to store the generated FLV files
os.makedirs('./tmp/', exist_ok=True)

# Generate FLV files with separate video and audio data sections
for i in range(1, 4):
    with open(f'./tmp/file_{i}.flv', 'wb') as f:
        # Simulating the generation of FLV files with separate video and audio data sections
        video_data = f'Video Data for File {i}'.encode()
        audio_data = f'Audio Data for File {i}'.encode()

        # FLV file structure with header, video data, audio data
        flv_header = b'FLV Header'
        flv_data = flv_header + video_data + audio_data

        f.write(flv_data)