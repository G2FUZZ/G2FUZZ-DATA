from moviepy.editor import VideoFileClip, concatenate_videoclips, VideoClip
import os
import json

# Directory to save the FLV file
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# FLV file properties
duration = 10  # seconds
width = 640
height = 360
fps = 24  # Frame per second

# Function to create frames with alpha channel
def make_frame(t):
    """Generates an RGBA image of the specified color. The alpha channel fades in."""
    import numpy as np
    frame = np.zeros((height, width, 4), dtype=np.uint8)
    frame[:, :, :3] = [255, 0, 0]  # RGB color
    frame[:, :, 3] = int(255 * t / duration)  # Alpha channel, fades in over time
    return frame

# Create a video clip with alpha channel
clip = VideoClip(make_frame, duration=duration).set_fps(fps)

# Specify the file path
file_path = os.path.join(output_dir, 'sample_with_alpha.flv')

# Write the video file with metadata and specifying the codec to support alpha channel
clip.write_videofile(file_path, codec='libx264', fps=fps, preset='ultrafast')

# Custom Metadata
custom_metadata = {
    "author": "John Doe",
    "description": "Sample FLV file with custom metadata",
    "keywords": ["sample", "flv", "metadata"]
}

# Convert custom metadata to JSON and save to a file
metadata_path = os.path.join(output_dir, 'sample_metadata.json')
with open(metadata_path, 'w') as json_file:
    json.dump(custom_metadata, json_file)

# Print the paths of the generated files
print(f"FLV file with Alpha Channel Support has been saved to {file_path}")
print(f"Custom Metadata JSON file has been saved to {metadata_path}")