import os

# Create a directory to store the generated FLV files
os.makedirs('./tmp/', exist_ok=True)

# Generate FLV files with different quality settings for video and audio streams, including live streaming feature
for i in range(1, 5):
    with open(f'./tmp/file_{i}.flv', 'wb') as f:
        # Simulating the generation of FLV files with live streaming feature
        if i == 4:
            quality_setting = f'Video Quality: {i} | Audio Quality: {i} | Cue Points: [0s, 10s, 20s] | Live streaming: FLV files support live streaming capabilities for broadcasting live events over the internet.'
        else:
            quality_setting = f'Video Quality: {i} | Audio Quality: {i} | Cue Points: [0s, 10s, 20s]'
        f.write(quality_setting.encode())