import os

def generate_complex_flv_file(file_path, metadata={}, video_tags=[], audio_tags=[]):
    # Create the directory if it doesn't exist
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, 'wb') as f:
        # Write FLV header
        f.write(b'FLV\x01\x05\x00\x00\x00\x09\x00\x00\x00\x00')
        
        # Write metadata
        for key, value in metadata.items():
            f.write(f'\x02{key}\x00{value}\x00'.encode())

        # Write video tags
        for tag in video_tags:
            f.write(tag)

        # Write audio tags
        for tag in audio_tags:
            f.write(tag)

    print(f"FLV file '{file_path}' with complex features generated and saved successfully.")

# Define metadata, video tags, and audio tags
metadata = {'duration': '60', 'width': '1920', 'height': '1080'}
video_tags = [b'\x09\x00\x00\x00\x00', b'\x05\x00\x00\x00\x00']
audio_tags = [b'\x04\x00\x00\x00\x00']

# Generate a complex FLV file
generate_complex_flv_file('./tmp/complex_file.flv', metadata=metadata, video_tags=video_tags, audio_tags=audio_tags)