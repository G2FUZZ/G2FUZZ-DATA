import cv2
import numpy as np
import os
import json

# Ensure the ./tmp/ directory exists
output_directory = './tmp/'
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Define the filenames of the output video file and the custom object and scene representation file
output_filename_hevc = output_directory + 'streaming_example_hevc.mp4'
custom_obj_scene_filename = output_directory + 'custom_obj_scene.json'

# Define the properties of the output video
frame_width = 640
frame_height = 480
fps = 24  # Frames per second
duration_sec = 5  # Duration of the video in seconds

# Define the codec for HEVC (High Efficiency Video Coding) and create VideoWriter object
fourcc_hevc = cv2.VideoWriter_fourcc(*'hvc1')  # Use 'HEVC' or 'hvc1' depending on platform support
out_hevc = cv2.VideoWriter(output_filename_hevc, fourcc_hevc, fps, (frame_width, frame_height))

# Initialize the custom object and scene representation container
custom_obj_scene_data = {
    "frames": []
}

for i in range(fps * duration_sec):
    # Create a frame with a solid color that changes over time
    frame = np.zeros((frame_height, frame_width, 3), dtype=np.uint8)
    color_intensity = (i * 255 // (fps * duration_sec))
    frame[:, :] = [color_intensity % 255, (color_intensity * 2) % 255, (color_intensity * 3) % 255]
    
    # Write the frame into the file using HEVC codec
    out_hevc.write(frame)

    # Append a custom representation for each frame to the data container
    custom_obj_scene_data["frames"].append({
        "frame_index": i,
        "object": {
            "type": "rectangle",
            "color": [color_intensity % 255, (color_intensity * 2) % 255, (color_intensity * 3) % 255],
            "position": {"x": 0, "y": 0},
            "size": {"width": frame_width, "height": frame_height}
        },
        "scene": {
            "description": "A frame with a solid color changing over time"
        }
    })

# Release the VideoWriter object for HEVC
out_hevc.release()

# Save the custom object and scene representation to a JSON file
with open(custom_obj_scene_filename, 'w') as f:
    json.dump(custom_obj_scene_data, f, indent=4)

print(f'HEVC video file has been saved to {output_filename_hevc}')
print(f'Custom object and scene representation file has been saved to {custom_obj_scene_filename}')