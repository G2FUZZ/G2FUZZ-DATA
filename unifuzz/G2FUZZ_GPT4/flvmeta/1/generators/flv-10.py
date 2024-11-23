from moviepy.editor import ColorClip, VideoClip
import os

# Directory to save the FLV file
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# FLV file properties
duration = 10  # seconds
width = 640
height = 360
fps = 24  # Frame per second

# Function to create frames with alpha channel
def make_frame(t):
    """Generates an RGBA image of the specified color. The alpha channel fades in."""
    import numpy as np
    frame = np.zeros((height, width, 4), dtype=np.uint8)
    frame[:, :, :3] = [255, 0, 0]  # RGB color
    frame[:, :, 3] = int(255 * t / duration)  # Alpha channel, fades in over time
    return frame

# Create a video clip with alpha channel
clip = VideoClip(make_frame, duration=duration).set_fps(fps)

# Specify the file path
file_path = os.path.join(output_dir, 'sample_with_alpha.flv')

# Write the video file with metadata and specifying the codec to support alpha channel
clip.write_videofile(file_path, codec='libx264', fps=fps, preset='ultrafast', ffmpeg_params=["-vcodec", "flv"])

print(f"FLV file with Alpha Channel Support has been saved to {file_path}")