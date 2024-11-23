import os

# Create a directory to store the generated FLV files
os.makedirs('./tmp/', exist_ok=True)

# Generate FLV files with advanced features
for i in range(1, 5):
    with open(f'./tmp/file_{i}.flv', 'wb') as f:
        # Simulating the generation of FLV files with advanced features
        if i == 4:
            metadata = {
                'title': 'Sample Title',
                'author': 'John Doe',
                'description': 'This is a sample FLV file with advanced features',
                'creation_date': '2022-01-01'
            }
            script_data = b'My FLV script data'
            cue_points = {
                'cue_point_1': {'time': '0s', 'payload': 'Cue Point 1 Data'},
                'cue_point_2': {'time': '10s', 'payload': 'Cue Point 2 Data'},
                'cue_point_3': {'time': '20s', 'payload': 'Cue Point 3 Data'}
            }
            f.write(f'Metadata: {metadata}\nScript Data: {script_data}\nCue Points: {cue_points}\nLive streaming: FLV files support live streaming capabilities for broadcasting live events over the internet.'.encode())
        else:
            quality_setting = f'Video Quality: {i} | Audio Quality: {i} | Cue Points: [0s, 10s, 20s]'
            f.write(quality_setting.encode())