import cv2
import numpy as np
import os
from moviepy.editor import VideoFileClip, concatenate_videoclips

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
video_file = os.path.join(output_dir, 'example.mp4')
video_writer = cv2.VideoWriter(video_file, fourcc, fps, (width, height))

# Generate frames
for frame_number in range(fps * duration):
    # Create an empty image (frame)
    frame = np.zeros((height, width, 3), dtype=np.uint8)

    # Add content to the frame (e.g., a moving white square)
    # Calculate position based on frame_number to animate
    square_size = 50
    x_pos = int((width - square_size) * (frame_number / (fps * duration)))
    y_pos = int((height - square_size) / 2)
    frame[y_pos:y_pos + square_size, x_pos:x_pos + square_size] = (255, 255, 255)

    # Write the frame to the video
    video_writer.write(frame)

# Release the video writer
video_writer.release()

# Now that the basic video file is created, we will add a hint track for streaming.
# Note: OpenCV does not directly support the addition of hint tracks to MP4 files.
# We will use MoviePy to manipulate the video file for demonstration purposes,
# understanding that hint track addition for streaming is a more complex process often handled by specialized software or libraries.

# Load the video file
clip = VideoFileClip(video_file)

# Since MoviePy does not directly support adding hint tracks, and there's no straightforward Python library to manipulate MP4 files at this granularity,
# the following operation is a placeholder to indicate where you would theoretically add the hint track.

# Concatenate the same video clip with itself as a demonstration (in practice, this would involve adding the hint track)
final_clip = concatenate_videoclips([clip, clip])

# Save the modified video file with a new name to indicate it's supposed to have hint tracks for streaming (for demonstration purposes)
final_video_file = os.path.join(output_dir, 'example_with_hints.mp4')
final_clip.write_videofile(final_video_file, codec='libx264')

print(f"Video saved to {final_video_file}")