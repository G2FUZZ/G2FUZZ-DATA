import os
from moviepy.editor import ColorClip, concatenate_videoclips

# Ensure the tmp directory exists
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define the parameters for the video
duration = 10  # Duration in seconds
size = (640, 360)  # Size of the video
fps = 24  # Frames per second

# Create a simple color clip, as an example of video content.
# This will serve as a demonstration of the FLV format's capability for streaming.
clip1 = ColorClip(size=size, color=(255, 0, 0), duration=duration)
clip2 = ColorClip(size=size, color=(0, 255, 0), duration=duration)
clip3 = ColorClip(size=size, color=(0, 0, 255), duration=duration)

# Concatenating clips to simulate a real video
final_clip = concatenate_videoclips([clip1, clip2, clip3], method="compose")

# Specify the output file path
output_path = os.path.join(output_dir, "example_stream.flv")

# Write the video file in FLV format
final_clip.write_videofile(output_path, codec="flv", fps=fps)

print(f"Video saved to {output_path}")