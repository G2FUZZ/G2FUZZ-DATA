import cv2
import numpy as np
import os

# Ensure the tmp directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Define the output path for the interactive video
output_path_interactive = os.path.join(output_dir, "example_interactive_streaming.mp4")

# Video properties
width, height = 640, 360
fps = 24
duration_sec = 5
background_color = (255, 0, 0)  # Red background
font = cv2.FONT_HERSHEY_SIMPLEX
text = "Interactive Video"
font_scale = 1
font_color = (255, 255, 255)  # White text
text_thickness = 2
text_size, _ = cv2.getTextSize(text, font, font_scale, text_thickness)
text_x = (width - text_size[0]) // 2
text_y = (height + text_size[1]) // 2

# Additional interactivity properties
toggle_text = False  # Toggle for displaying text

# Initialize video writer with ISOBMFF (mp4v) compatibility
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_writer_interactive = cv2.VideoWriter(output_path_interactive, fourcc, fps, (width, height))

# Generate each frame with interactivity
for frame_number in range(fps * duration_sec):
    frame = np.zeros((height, width, 3), dtype=np.uint8)
    frame[:] = background_color
    
    # Toggle text display every second
    if frame_number % fps == 0:
        toggle_text = not toggle_text
    
    # If toggle is true, display text
    if toggle_text:
        cv2.putText(frame, text, (text_x, text_y), font, font_scale, font_color, text_thickness)
    else:
        # Display an alternative text or interactive element
        alt_text = "Click Me!"
        alt_text_size, _ = cv2.getTextSize(alt_text, font, font_scale, text_thickness)
        alt_text_x = (width - alt_text_size[0]) // 2
        alt_text_y = (height // 2 + alt_text_size[1] * 3)  # Position it below the main text
        cv2.putText(frame, alt_text, (alt_text_x, alt_text_y), font, font_scale, font_color, text_thickness)
    
    video_writer_interactive.write(frame)

# Release the video writer
video_writer_interactive.release()

print(f"Interactive Video saved to {output_path_interactive}")