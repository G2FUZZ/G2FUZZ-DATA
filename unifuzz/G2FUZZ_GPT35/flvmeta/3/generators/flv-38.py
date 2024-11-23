import os

def generate_complex_flv_file(file_path):
    # Create a directory to save the generated FLV files
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, 'wb') as file:
        # Write FLV header
        file.write(b'FLV\x01\x05\x00\x00\x00\x09\x00\x00\x00\x00')

        # Write video tags with H.264 codec
        video_tag1 = b'\x09\x00\x00\x00\x00\x00\x00\x00\x00'
        video_tag2 = b'\x09\x00\x00\x00\x00\x01\x00\x00\x00'
        file.write(video_tag1)
        file.write(video_tag2)

        # Write audio tags with AAC codec
        audio_tag1 = b'\x08\x00\x00\x00\x00\x02\x00\x00\x00'
        audio_tag2 = b'\x08\x00\x00\x00\x00\x03\x00\x00\x00'
        file.write(audio_tag1)
        file.write(audio_tag2)

        # Write metadata tag
        metadata_tag = b'\x12\x00\x00\x00\x00\x00\x00\x00\x2b\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00onMetaData\x08\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x0a\x40\x3f\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        file.write(metadata_tag)

    print(f"Complex FLV file generated and saved at: {file_path}")

# Generate FLV file with multiple video and audio tracks, metadata information, and timestamp synchronization
file_path = './tmp/complex_flv_file.flv'
generate_complex_flv_file(file_path)