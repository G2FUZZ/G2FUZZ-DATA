import cv2
import numpy as np
import os
import json

# Ensure the ./tmp/ directory exists
output_directory = './tmp/'
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Define the filename of the output video file
output_filename = output_directory + 'enhanced_streaming_example.mp4'

# Define the properties of the output video
frame_width = 640
frame_height = 480
fps = 24  # Frames per second
duration_sec = 10  # Duration of the video in seconds

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_filename, fourcc, fps, (frame_width, frame_height))

# Initialize a list to store complex object descriptors
complex_object_descriptors = []

for i in range(fps * duration_sec):
    # Create a frame with a solid background color that changes over time
    frame = np.zeros((frame_height, frame_width, 3), dtype=np.uint8)
    background_color_intensity = (i * 255 // (fps * duration_sec))
    frame[:, :] = [background_color_intensity % 255, (background_color_intensity * 2) % 255, (background_color_intensity * 5) % 255]
    
    # Add animated text to the frame
    font = cv2.FONT_HERSHEY_SIMPLEX
    text = f"Frame {i}"
    cv2.putText(frame, text, (50, frame_height - 50), font, 1, (255-background_color_intensity % 255, 255-(background_color_intensity * 2) % 255, 255-(background_color_intensity * 5) % 255), 2, cv2.LINE_AA)
    
    # Draw varying rectangle shapes
    top_left_corner = (i % frame_width, i % frame_height)
    bottom_right_corner = ((i * 2) % frame_width, (i * 2) % frame_height)
    cv2.rectangle(frame, top_left_corner, bottom_right_corner, (255-background_color_intensity % 255, 100, 100), 3)
    
    # Write the frame into the file
    out.write(frame)

    # Add a complex object descriptor for each frame
    descriptor = {
        "frame": i,
        "background_color_intensity": background_color_intensity,
        "background_color": {
            "R": background_color_intensity % 255,
            "G": (background_color_intensity * 2) % 255,
            "B": (background_color_intensity * 5) % 255
        },
        "text": text,
        "rectangle": {
            "top_left": top_left_corner,
            "bottom_right": bottom_right_corner
        }
    }
    complex_object_descriptors.append(descriptor)

# Close the video file
out.release()

# Save the complex object descriptors to a JSON file
descriptors_filename = output_directory + 'enhanced_streaming_example_descriptors.json'
with open(descriptors_filename, 'w') as file:
    json.dump(complex_object_descriptors, file, indent=4)

print(f'Enhanced video file has been saved to {output_filename}')
print(f'Complex object descriptors have been saved to {descriptors_filename}')