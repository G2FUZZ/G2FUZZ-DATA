import cv2
import numpy as np
import os

# Ensure the tmp directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Video properties
width, height = 640, 480
fps = 24
duration = 5  # seconds
fourcc = cv2.VideoWriter_fourcc(*'avc1')  # AVC / H.264 codec
output_filename = os.path.join(output_dir, 'example_hdr.mp4')

# Create a video writer object with 10-bit color depth for HDR
# Note: OpenCV does not directly support HDR video creation. This is a conceptual extension.
# In practice, generating HDR content involves capturing or rendering content in a format
# that supports wider color gamuts and higher dynamic range (e.g., using 10 or 12-bit color depth instead of standard 8 bits).
# This might require using specialized software or libraries designed for HDR video processing.
out = cv2.VideoWriter(output_filename, fourcc, fps, (width, height))

# Generate frames
for i in range(duration * fps):
    # Create a black image with a higher bit depth. While OpenCV defaults to 8 bits (0-255),
    # HDR would typically use a higher bit depth. This is simulated here by using a normal 8-bit image.
    # Actual HDR content creation would require support for higher bit depths and appropriate color spaces (e.g., BT.2020).
    frame = np.zeros((height, width, 3), dtype=np.uint8)
    
    # Calculate the square's position to create a moving effect
    center_x = int((width // 2) + (width // 4) * np.sin(2 * np.pi * i / (fps * 2)))
    center_y = int((height // 2) + (height // 4) * np.cos(2 * np.pi * i / (fps * 2)))
    start_point = (center_x - 50, center_y - 50)
    end_point = (center_x + 50, center_y + 50)
    
    # Draw a blue square. In a real HDR scenario, you would use a wider range of colors and intensities.
    cv2.rectangle(frame, start_point, end_point, (255, 0, 0), -1)
    
    # Write the frame to the video file
    out.write(frame)

# Release the video writer
out.release()
print(f"Video saved as {output_filename}")