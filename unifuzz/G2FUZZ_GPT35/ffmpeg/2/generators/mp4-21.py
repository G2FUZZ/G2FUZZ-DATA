import os

# Create a directory to store the generated mp4 files
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample mp4 file with the specified features
features = [
    'MP4 file with streaming support: efficient compression and compatibility with streaming protocols.',
    '360-degree video support: MP4 files can store 360-degree video content for immersive viewing experiences on compatible platforms.'
]

with open('./tmp/360_video_support.mp4', 'wb') as file:
    for feature in features:
        file.write(feature.encode('utf-8') + b'\n')