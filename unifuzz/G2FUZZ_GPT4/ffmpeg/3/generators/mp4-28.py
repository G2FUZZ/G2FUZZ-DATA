import cv2
import numpy as np
import os

def create_video(output_file, codec='avc1'):
    # Ensure the output directory exists
    output_dir = os.path.dirname(output_file)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Video properties
    width, height = 640, 480
    fps = 24
    duration = 5  # seconds
    fourcc = cv2.VideoWriter_fourcc(*codec)  # Dynamically set codec

    # Create a VideoWriter object
    out = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

    # Generate synthetic frames
    for t in range(fps * duration):
        # Create a frame with changing colors
        frame = np.zeros((height, width, 3), dtype=np.uint8)
        frame[:, :, 0] = (t * 5) % 256  # Red channel
        frame[:, :, 1] = (t * 3) % 256  # Green channel
        frame[:, :, 2] = (t * 1) % 256  # Blue channel
        
        # Write the frame to the video file
        out.write(frame)

    # Release the VideoWriter object
    out.release()

    print(f"Video file has been saved to {output_file}")

# Generate videos with different codecs to demonstrate codec independence
create_video('./tmp/example_avc.mp4', 'avc1')  # Using H.264
create_video('./tmp/example_hevc.mp4', 'hevc')  # Using H.265/HEVC