import os

def generate_extended_flv_file(file_path, metadata={}, video_tags=[], audio_tags=[]):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, 'wb') as f:
        f.write(b'FLV\x01\x05\x00\x00\x00\x09\x00\x00\x00\x00')

        for key, value in metadata.items():
            f.write(f'\x02{key}\x00{value}\x00'.encode())

        for tag in video_tags:
            f.write(tag)

        for tag in audio_tags:
            f.write(tag)

        # Add more video and audio tags with different codecs and timestamps
        f.write(b'\x09\x00\x00\x00\x01')  # Video tag with codec ID 1
        f.write(b'\x09\x00\x00\x00\x02')  # Video tag with codec ID 2
        f.write(b'\x04\x00\x00\x00\x01')  # Audio tag with codec ID 1
        f.write(b'\x04\x00\x00\x00\x02')  # Audio tag with codec ID 2

    print(f"Extended FLV file '{file_path}' with more complex features generated and saved successfully.")

# Define extended metadata, video tags, and audio tags
metadata = {'duration': '120', 'width': '1920', 'height': '1080', 'bitrate': '5000'}
video_tags = [b'\x09\x00\x00\x00\x03', b'\x05\x00\x00\x00\x01']
audio_tags = [b'\x04\x00\x00\x00\x01', b'\x04\x00\x00\x00\x02']

# Generate an extended FLV file
generate_extended_flv_file('./tmp/extended_file.flv', metadata=metadata, video_tags=video_tags, audio_tags=audio_tags)