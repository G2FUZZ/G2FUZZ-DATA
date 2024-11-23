import os

# Create a directory to store the generated FLV files
os.makedirs('./tmp/', exist_ok=True)

# Generate FLV files with more complex file features
for i in range(1, 6):
    with open(f'./tmp/file_{i}.flv', 'wb') as f:
        # Simulating the generation of FLV files with more complex features
        metadata = {
            'title': f'Video Title {i}',
            'author': 'John Doe',
            'description': f'This is a sample video with complex features {i}',
            'creation_date': '2022-01-01',
            'duration': '00:01:30',
            'resolution': '1920x1080',
            'bitrate': '5000 kbps'
        }
        f.write(f'METADATA: {metadata}\n'.encode())

        for j in range(1, 4):
            video_stream = f'Video Stream {j} | Resolution: 1920x1080 | Bitrate: 5000 kbps'
            audio_stream = f'Audio Stream {j} | Bitrate: 128 kbps'
            f.write(f'VIDEO: {video_stream}\n'.encode())
            f.write(f'AUDIO: {audio_stream}\n'.encode())

        custom_tags = {
            'custom_tag_1': 'value_1',
            'custom_tag_2': 'value_2',
            'custom_tag_3': 'value_3'
        }
        f.write(f'CUSTOM TAGS: {custom_tags}\n'.encode())