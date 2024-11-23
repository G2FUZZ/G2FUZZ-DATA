import cv2
import numpy as np
import os

# Ensure the ./tmp/ directory exists
output_directory = './tmp/'
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Define the filename of the output video file including HEVC feature
output_filename_hevc_frag = output_directory + 'streaming_example_hevc_fragmented.mp4'

# Define the properties of the output video
frame_width = 640
frame_height = 480
fps = 24  # Frames per second
duration_sec = 5  # Duration of the video in seconds

# Define the codec for HEVC (High Efficiency Video Coding) and create VideoWriter object
fourcc_hevc = cv2.VideoWriter_fourcc(*'hvc1')  # Use 'HEVC' or 'hvc1' depending on platform support

# VideoWriter with file fragmentation enabled. The `cv2.VIDEOWRITER_PROP_FRAMES` property
# is not directly applicable for enabling fragmentation. Instead, we use the appropriate
# container format and settings through OpenCV's VideoWriter, if available.
# Since OpenCV does not directly expose file fragmentation, this might require post-processing
# with external tools or using a custom container writer. Here, we proceed with a placeholder
# for the standard VideoWriter as the direct method. For actual fragmentation, consider using
# ffmpeg or similar tools to post-process the video file.
out_hevc_frag = cv2.VideoWriter(output_filename_hevc_frag, fourcc_hevc, fps, (frame_width, frame_height))

for i in range(fps * duration_sec):
    # Create a frame with a solid color that changes over time
    frame = np.zeros((frame_height, frame_width, 3), dtype=np.uint8)
    color_intensity = (i * 255 // (fps * duration_sec))
    frame[:, :] = [color_intensity % 255, (color_intensity * 2) % 255, (color_intensity * 3) % 255]
    
    # Write the frame into the file using HEVC codec
    out_hevc_frag.write(frame)

# Release the VideoWriter object for HEVC with fragmentation (conceptual, see note above)
out_hevc_frag.release()
print(f'HEVC video file with fragmentation (conceptually) has been saved to {output_filename_hevc_frag}')