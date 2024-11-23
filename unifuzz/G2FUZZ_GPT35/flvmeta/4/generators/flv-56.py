import os
import struct

def write_flv_file(file_path, video_data, audio_data, metadata):
    with open(file_path, 'wb') as f:
        # FLV file structure with header, previous tag size, tag headers, video data, audio data, metadata
        flv_header = b'FLV' + struct.pack('BBB', 1, 5, 0)
        previous_tag_size = struct.pack('>I', 0)
        
        # Tag structure for video data
        video_tag_header = struct.pack('>BBHBB', 9, len(video_data) >> 16, len(video_data) & 0xFFFF, 0, 0)
        
        # Tag structure for audio data
        audio_tag_header = struct.pack('>BBHBB', 8, len(audio_data) >> 16, len(audio_data) & 0xFFFF, 0, 0)
        
        flv_data = flv_header + previous_tag_size + video_tag_header + video_data + previous_tag_size + audio_tag_header + audio_data + metadata
        f.write(flv_data)

# Create a directory to store the generated FLV files
os.makedirs('./tmp/', exist_ok=True)

# Generate FLV files with more complex file structures
for i in range(1, 4):
    video_data = f'Video Data for File {i}'.encode()
    audio_data = f'Audio Data for File {i}'.encode()
    metadata = b'Metadata for File {i}'

    write_flv_file(f'./tmp/file_{i}.flv', video_data, audio_data, metadata)