from moviepy.editor import ColorClip, concatenate_videoclips
from moviepy.video.fx.all import even_size
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create a list of color clips (acting as different parts of the video) with keyframes
# Each color clip will be 2 seconds long
clips = []
# Define colors using RGB tuples
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]  # red, green, blue, yellow
for color in colors:
    clip = ColorClip(size=(640, 480), color=color, duration=2)
    clip = even_size(clip)  # Ensure size is even (required for some codecs)
    clips.append(clip)

# Concatenate the color clips into one video
final_clip = concatenate_videoclips(clips)

# Save the video as an FLV file with keyframes
output_file = os.path.join(output_dir, 'example.flv')
# Specify the fps in the write_videofile function
final_clip.write_videofile(output_file, codec='flv', fps=24)

print(f"Video saved to {output_file}")