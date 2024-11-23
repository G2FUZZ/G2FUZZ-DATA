import cv2
import numpy as np
import os

# Ensure the tmp directory exists
output_directory = './tmp/'
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Initialize video settings for 360-degree video
frame_width = 2048  # A common width for 360-degree videos
frame_height = 1024  # A common height for 360-degree videos, equirectangular format
fps = 24
output_filename = output_directory + '360_degree_video.mp4'

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_filename, fourcc, fps, (frame_width, frame_height))

# Generate a basic 360-degree video with 60 frames (2.5 seconds at 24 FPS)
for i in range(60):
    # Create a frame with random colors
    # For a more immersive 360-degree experience, you'd generate or use spherical/equirectangular images
    frame = np.random.randint(0, 255, (frame_height, frame_width, 3), dtype=np.uint8)
    out.write(frame)

# Release everything when the job is finished
out.release()
cv2.destroyAllWindows()

print(f"360-Degree Video created: {output_filename}")

# Note: This code generates a basic 360-degree MP4 file with random colors for demonstration.
# For true 360-degree videos, you would use equirectangular images or videos and possibly metadata
# to inform players that the video is 360-degree. This example does not include the injection of metadata
# or the production of real 360-degree content, which would require specific capture techniques or simulations.