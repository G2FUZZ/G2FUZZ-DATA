import os
from moviepy.editor import ColorClip, concatenate_videoclips

# Create the tmp/ directory if it does not exist
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define the path for the output FLV file
flv_file_path = os.path.join(output_dir, "sample_loop.flv")

# Create a simple color clip, here a 5-second red clip in 640x480.
clip = ColorClip(size=(640, 480), color=(255, 0, 0), duration=5)

# To implement looping, let's duplicate the clip and concatenate it with itself.
# For example, to create a loop that repeats the clip 3 times:
loop_count = 3  # Number of times the clip should loop
looped_clip = concatenate_videoclips([clip] * loop_count)

# Write the looped clip to a .flv file
looped_clip.write_videofile(flv_file_path, codec="libx264", fps=24, audio=False)