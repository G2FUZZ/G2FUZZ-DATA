import os

# Create a directory if it does not exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate FLV file with the specified features including Frame Accuracy
feature = """
Cross-Platform Compatibility: FLV files are widely supported across different platforms and devices, making them a popular choice for sharing and distributing video content online.
Frame Accuracy: FLV files ensure frame-accurate playback, maintaining synchronization between audio and video frames for precise timing and smooth viewing experience.
"""

file_path = os.path.join(directory, 'extended_file.flv')

with open(file_path, 'w') as file:
    file.write(feature)

print(f"FLV file with the specified features including Frame Accuracy has been generated and saved at: {file_path}")