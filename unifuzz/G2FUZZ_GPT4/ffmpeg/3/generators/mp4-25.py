import cv2
import numpy as np
import os
import textwrap

# Ensure the output directory exists
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Parameters for the video
width, height = 640, 480
fps = 24
duration_sec = 5
background_color = (255, 255, 255)  # White background

# Prepare text to display in the video
features = [
    "Compatibility: MP4 files are widely supported by various devices and platforms, "
    "including smartphones, tablets, PCs, and smart TVs, ensuring that content is accessible "
    "to a broad audience.",
    "B-Frames Support: MP4 supports B-frames (bi-directional frames), enhancing video compression "
    "efficiency by allowing certain frames to reference both previous and subsequent frames, "
    "leading to better video quality at lower bitrates.",
    "Movie Fragments: MP4 supports movie fragments (moof atoms) which allow for the division of "
    "the file into smaller, independently decodable fragments. This improves the efficiency of "
    "editing and streaming operations, especially for large videos."
]
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
font_color = (0, 0, 0)  # Black text
thickness = 2
line_spacing = 10  # Spacing between lines

# Prepare the video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec used to create the video
video_filename = os.path.join(output_dir, "features.mp4")
out = cv2.VideoWriter(video_filename, fourcc, fps, (width, height))

for feature in features:
    wrapped_text = textwrap.wrap(feature, width=60)  # Wrap the text to fit the screen
    # Calculate an initial text size using the first line or a sample text
    if wrapped_text:  # Ensure there is at least one line
        sample_text_size = cv2.getTextSize(wrapped_text[0], font, font_scale, thickness)[0]
    else:
        sample_text_size = (0, 0)  # Default to zero if no text
    # Calculate the starting Y position to center the text block vertically
    total_text_height = (len(wrapped_text) * (sample_text_size[1] + line_spacing)) - line_spacing
    current_y = (height - total_text_height) // 2

    for _ in range(fps * duration_sec // len(features)):
        frame = np.full((height, width, 3), background_color, np.uint8)
        for line in wrapped_text:
            # Recalculate text size for wrapped lines
            text_size = cv2.getTextSize(line, font, font_scale, thickness)[0]
            text_x = (width - text_size[0]) // 2
            cv2.putText(frame, line, (text_x, current_y), font, font_scale, font_color, thickness)
            current_y += text_size[1] + line_spacing  # Move to the next line position
        out.write(frame)
        # Reset Y position for the next frame
        current_y = (height - total_text_height) // 2

# Release the video writer
out.release()

print(f"Video saved as {video_filename}")