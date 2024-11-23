import cv2
import numpy as np
import os

# Ensure the output directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Define the output file path
output_file = os.path.join(output_dir, 'enhanced_streaming_video.mp4')

# Video properties
width, height = 640, 480
fps = 24  # Frames per second
duration = 10  # seconds
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Define codec

# Create a VideoWriter object
out = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

# Prepare an overlay with transparent background (for vector graphics)
overlay = np.zeros((height, width, 4), dtype=np.uint8)

# Draw a vector graphic (e.g., a moving circle) on the overlay
for i in range(fps * duration):
    # Create a frame with synthetic content
    frame = np.zeros((height, width, 3), dtype=np.uint8)
    color_value = int((i / (fps * duration)) * 255)
    frame[:, :] = [color_value, 0, 255 - color_value]  # BGR format
    
    # Reset overlay
    overlay.fill(0)
    
    # Define circle properties
    center = (int(width * (i / (fps * duration))), height // 2)
    radius = 50
    color = (0, 255, 0, 127)  # RGBA: green with 50% opacity
    thickness = -1  # Filled circle
    
    # Draw circle on the overlay
    cv2.circle(overlay, center, radius, color, thickness)
    
    # Convert overlay to BGR and merge with the frame
    bgr_overlay = cv2.cvtColor(overlay, cv2.COLOR_BGRA2BGR)
    frame_with_overlay = cv2.addWeighted(frame, 1.0, bgr_overlay, 1.0, 0)
    
    # Write the frame with overlay to the video file
    out.write(frame_with_overlay)

# Release the VideoWriter object
out.release()

print(f"Video saved to {output_file}")