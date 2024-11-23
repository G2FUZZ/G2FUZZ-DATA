import cv2
import numpy as np
import os
from mutagen.mp4 import MP4, MP4Cover, MP4Tags

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Video properties
width, height = 640, 480
fps = 24
duration = 5  # seconds
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Using 'mp4v' for H.264 encoding

# Initialize video writer
video_file = os.path.join(output_dir, 'example_with_userdata.mp4')
video_writer = cv2.VideoWriter(video_file, fourcc, fps, (width, height))

# Generate frames
for frame_number in range(fps * duration):
    # Create an empty image (frame)
    frame = np.zeros((height, width, 3), dtype=np.uint8)

    # Add content to the frame (e.g., a moving white square)
    # Calculate position based on frame_number to animate
    square_size = 50
    x_pos = int((width - square_size) * (frame_number / (fps * duration)))
    y_pos = int((height - square_size) / 2)  # Corrected from square_field to square_size
    frame[y_pos:y_pos + square_size, x_pos:x_pos + square_size] = (255, 255, 255)

    # Write the frame to the video
    video_writer.write(frame)

# Release the video writer
video_writer.release()

# Adding User Data
mp4_file = MP4(video_file)
mp4_file["\xa9nam"] = "Example Video with User Data"
mp4_file["\xa9alb"] = "Example Album/Project"
mp4_file["\xa9art"] = "Example Artist/Creator"
mp4_file["\xa9day"] = "2023"
mp4_file["desc"] = "This is an example video incorporating user data for demonstration purposes."
mp4_file["cprt"] = "Copyright 2023 Example Creator"

# You can also add cover art to the MP4 file
# with open("cover.jpg", "rb") as cover_file:
#     mp4_file["covr"] = [MP4Cover(cover_file.read(), imageformat=MP4Cover.FORMAT_JPEG)]

mp4_file.save()

print(f"Video saved to {video_file} with User Data")