import struct

# Function to generate FLV file with video and audio data
def generate_flv_file(file_path):
    # FLV header
    flv_header = b'FLV\x01\x05\x00\x00\x00\x09\x00\x00\x00\x00'

    # FLV metadata
    metadata = b'\x02\x00\x0d\x40\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

    # FLV video and audio data
    video_data = b'\x09\x00\x00\x00\x02\x00\x00\x00\x00'
    audio_data = b'\x08\x00\x00\x00\x02\x00\x00\x00\x00'

    # Writing FLV data to the file
    with open(file_path, 'wb') as file:
        file.write(flv_header)
        file.write(struct.pack('>I', len(metadata)))
        file.write(metadata)
        file.write(struct.pack('>I', len(video_data)))
        file.write(video_data)
        file.write(struct.pack('>I', len(audio_data)))
        file.write(audio_data)

# Generate FLV file with complex features
generate_flv_file('./tmp/complex_file.flv')