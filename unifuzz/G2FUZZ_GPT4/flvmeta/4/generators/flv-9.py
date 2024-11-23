from moviepy.editor import ColorClip
from moviepy.video.fx import resize
import os
import json

# Ensure the tmp directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define the output file path
output_file = os.path.join(output_dir, 'sample_with_cue_points.flv')

# Generate a simple video clip (e.g., a 5-second red screen)
clip = ColorClip(size=(640, 360), color=(255, 0, 0), duration=5)

# Optional: Resize the clip if needed
# clip = clip.fx(resize, width=640) # Example of resizing, modify as needed

# Define cue points as a list of dictionaries
# Each cue point could have a 'time' in seconds and 'name' as a string
cue_points = [
    {"time": 1, "name": "CuePoint1"},
    {"time": 3, "name": "CuePoint2"}
]

# Write the video file with the H.264 codec within an FLV container
# Note: MoviePy does not natively support embedding cue points within FLV files.
# As a workaround, we will create a separate JSON file to store cue points.
clip.write_videofile(output_file, codec='libx264', fps=24)

# Create a JSON file to store cue points
cue_points_file = os.path.splitext(output_file)[0] + '_cue_points.json'
with open(cue_points_file, 'w') as f:
    json.dump(cue_points, f)

print(f"Video file saved: {output_file}")
print(f"Cue points saved: {cue_points_file}")