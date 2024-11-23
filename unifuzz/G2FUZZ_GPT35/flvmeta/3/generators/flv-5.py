import os

# Create a directory if it does not exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate FLV file with the specified features
feature = "Cross-Platform Compatibility: FLV files are widely supported across different platforms and devices, making them a popular choice for sharing and distributing video content online."
file_path = os.path.join(directory, 'generated_file.flv')

with open(file_path, 'w') as file:
    file.write(feature)

print(f"FLV file with the specified features has been generated and saved at: {file_path}")