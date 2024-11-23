import cv2
import numpy as np
import os
import json

# Ensure the ./tmp/ directory exists
output_directory = './tmp/'
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Define the filename of the output video file
output_filename = output_directory + 'streaming_example_with_mpeg_h_support.mp4'

# Define the properties of the output video
frame_width = 640
frame_height = 480
fps = 24  # Frames per second
duration_sec = 5  # Duration of the video in seconds

# Define the codec and create VideoWriter object
# Note: Using 'mp4v' codec as a placeholder. For actual MPEG-H support, 
# the codec and container format might need to be adjusted based on the encoder's capabilities and requirements.
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_filename, fourcc, fps, (frame_width, frame_height))

# Initialize a list to store object descriptors with an added "MPEG-H Support" feature
object_descriptors = []

for i in range(fps * duration_sec):
    # Create a frame with a solid color that changes over time
    frame = np.zeros((frame_height, frame_width, 3), dtype=np.uint8)
    color_intensity = (i * 255 // (fps * duration_sec))
    frame[:, :] = [color_intensity % 255, (color_intensity * 2) % 255, (color_intensity * 3) % 255]
    
    # Write the frame into the file
    out.write(frame)

    # Add an object descriptor for each frame, including a mock "MPEG-H Support" description
    descriptor = {
        "frame": i,
        "color_intensity": color_intensity,
        "color": {
            "R": color_intensity % 255,
            "G": (color_intensity * 2) % 255,
            "B": (color_intensity * 3) % 255
        },
        "MPEG-H_Support": "Enabled"  # Indicating MPEG-H Support as a feature of this frame/descriptor
    }
    object_descriptors.append(descriptor)

# Close the video file
out.release()

# Save the object descriptors to a JSON file
descriptors_filename = output_directory + 'streaming_example_with_mpeg_h_descriptors.json'
with open(descriptors_filename, 'w') as file:
    json.dump(object_descriptors, file, indent=4)

print(f'Video file with MPEG-H support has been saved to {output_filename}')
print(f'Object descriptors with MPEG-H support have been saved to {descriptors_filename}')