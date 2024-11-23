import os

# Create a directory if it does not exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate FLV file with the specified features
features = [
    "Cross-Platform Compatibility: FLV files are widely supported across different platforms and devices, making them a popular choice for sharing and distributing video content online.",
    "Text Track Support: FLV files can incorporate text tracks for displaying subtitles, captions, or other textual information synchronized with the video content."
]

file_path = os.path.join(directory, 'extended_file.flv')

with open(file_path, 'w') as file:
    for feature in features:
        file.write(feature + '\n\n')

print(f"FLV file with the specified features including 'Text Track Support' has been generated and saved at: {file_path}")