import os

# Create a directory if it does not exist
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Generate a sample FLV file with additional complex features
file_content = (
    "FLV files support streaming for progressive download and real-time streaming applications.\n"
    "Embedded Metadata: This FLV file contains metadata information about the video content.\n"
    "Multiple Audio/Video Tracks: The FLV file includes multiple audio and video tracks for different languages."
)

file_path = os.path.join(output_dir, 'complex_sample.flv')
with open(file_path, 'w') as file:
    file.write(file_content)

print(f"Complex FLV file generated successfully at: {file_path}")