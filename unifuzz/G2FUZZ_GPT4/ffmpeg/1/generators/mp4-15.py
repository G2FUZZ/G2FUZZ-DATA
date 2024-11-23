import cv2
import numpy as np
import os
import json

# Ensure the tmp directory exists
os.makedirs('./tmp', exist_ok=True)

# Define the video parameters
width, height = 640, 480
fps = 24
duration = 5  # seconds
output_file = './tmp/generated_video_with_description.mp4'
annotations_file = './tmp/generated_video_with_description_annotations.json'
description_file = './tmp/generated_video_with_description_info.json'

# Create a video writer object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

# Prepare a dictionary to hold annotations
annotations = []

# Prepare a dictionary for sample description
sample_description = {
    "video": {
        "codec": "mp4v",
        "width": width,
        "height": height,
        "fps": fps
    },
    "description": "This video contains a moving rectangle with annotations."
}

# Generate frames for the video
for frame_num in range(fps * duration):
    # Create a blank image
    img = np.zeros((height, width, 3), dtype=np.uint8)
    
    # Calculate the position of the rectangle
    x_start = int((width / (fps * duration)) * frame_num)
    y_start = height // 4
    x_end = x_start + 100
    y_end = y_start + 100
    
    # Draw a moving rectangle
    cv2.rectangle(img, (x_start, y_start), (x_end, y_end), (255, 0, 0), -1)
    
    # Write the frame to the video
    video.write(img)

    # Add an annotation for the current frame
    annotations.append({
        "frame": frame_num,
        "annotation": {
            "type": "rectangle",
            "position": {"x_start": x_start, "y_start": y_start, "x_end": x_end, "y_end": y_end},
            "color": "blue",
            "metadata": {
                "comment": "This is a moving rectangle",
                "link": "https://example.com"
            }
        }
    })

# Release the video writer
video.release()

# Save annotations to a file
with open(annotations_file, 'w') as f:
    json.dump(annotations, f, indent=4)

# Save sample description to a file
with open(description_file, 'w') as f:
    json.dump(sample_description, f, indent=4)

print(f"Video file has been saved to {output_file}")
print(f"Annotations file has been saved to {annotations_file}")
print(f"Sample description file has been saved to {description_file}")