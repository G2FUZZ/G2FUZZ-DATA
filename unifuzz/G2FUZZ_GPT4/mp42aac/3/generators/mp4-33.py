import cv2
import numpy as np
import os

# Ensure the ./tmp/ directory exists
output_directory = './tmp/'
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Define the filename of the output video file including HEVC feature
output_filename_hevc_frag = output_directory + 'streaming_example_hevc_fragmented.mp4'
# Define the filename for an auxiliary video stream
output_filename_aux = output_directory + 'auxiliary_stream.mp4'

# Define the properties of the output video
frame_width = 640
frame_height = 480
fps = 24  # Frames per second
duration_sec = 5  # Duration of the video in seconds

# Define the codec for HEVC (High Efficiency Video Coding)
fourcc_hevc = cv2.VideoWriter_fourcc(*'hvc1')  # Use 'HEVC' or 'hvc1' depending on platform support

# Create VideoWriter object for the main and auxiliary video streams
out_hevc_frag = cv2.VideoWriter(output_filename_hevc_frag, fourcc_hevc, fps, (frame_width, frame_height))
out_aux = cv2.VideoWriter(output_filename_aux, fourcc_hevc, fps, (frame_width, frame_height))

for i in range(fps * duration_sec):
    # Create a frame with a solid color that changes over time
    main_frame = np.zeros((frame_height, frame_width, 3), dtype=np.uint8)
    aux_frame = np.zeros((frame_height, frame_width, 3), dtype=np.uint8)
    color_intensity = (i * 255 // (fps * duration_sec))
    main_frame[:, :] = [color_intensity % 255, (color_intensity * 2) % 255, (color_intensity * 3) % 255]
    # Auxiliary frame will have a contrasting color pattern
    aux_frame[:, :] = [(255 - color_intensity) % 255, (255 - color_intensity * 2) % 255, (255 - color_intensity * 3) % 255]
    
    # Write the frame into the file using HEVC codec
    out_hevc_frag.write(main_frame)
    out_aux.write(aux_frame)

# Release the VideoWriter objects
out_hevc_frag.release()
out_aux.release()

print(f'HEVC video file with fragmentation (conceptually) has been saved to {output_filename_hevc_frag}')
print(f'Auxiliary video stream has been saved to {output_filename_aux}')