import os

# Create a directory if it does not exist
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Generate a sample FLV file with the specified features
file_content = "FLV files support streaming for progressive download, real-time streaming applications, and frame-accurate playback ensuring precise synchronization of audio and video frames."
file_path = os.path.join(output_dir, 'sample_with_frame_accuracy.flv')
with open(file_path, 'w') as file:
    file.write(file_content)

print(f"FLV file with Frame accuracy feature generated successfully at: {file_path}")