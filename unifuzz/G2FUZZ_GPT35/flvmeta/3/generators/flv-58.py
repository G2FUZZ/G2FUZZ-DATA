import os

# Create a directory if it does not exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate FLV file with more complex features
features = [
    "Video Codec: H.264 (High Efficiency Video Coding) for high-quality video compression.",
    "Audio Codec: AAC (Advanced Audio Coding) for high-quality audio compression.",
    "Frame Rate: 30 frames per second for smooth playback."
]

file_path = os.path.join(directory, 'extended_file.flv')

with open(file_path, 'w') as file:
    for feature in features:
        file.write(feature + '\n\n')

print(f"FLV file with the specified features including 'Video Codec', 'Audio Codec', and 'Frame Rate' has been generated and saved at: {file_path}")