from moviepy.editor import ColorClip, concatenate_videoclips
from moviepy.video.fx.all import even_size, speedx
import os
import subprocess

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create a list of color clips (acting as different parts of the video) with keyframes
# Each color clip will be 2 seconds long
clips = []
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]  # red, green, blue, yellow
for color in colors:
    clip = ColorClip(size=(640, 480), color=color, duration=2)
    clip = even_size(clip)  # Ensure size is even (required for some codecs)
    clips.append(clip)

# Concatenate the color clips into one video
final_clip = concatenate_videoclips(clips)

# Apply slow motion and fast motion effects
slow_motion_clip = speedx(final_clip.subclip(0, 2), factor=0.5)
fast_motion_clip = speedx(final_clip.subclip(2, 4), factor=2)

# Concatenate the modified clips back with the rest of the video
modified_clips = [slow_motion_clip, fast_motion_clip] + [final_clip.subclip(4, final_clip.duration)]
final_clip_with_effects = concatenate_videoclips(modified_clips)

# Save the intermediate video to use it with ffmpeg
intermediate_file = os.path.join(output_dir, 'intermediate_video.mp4')
final_clip_with_effects.write_videofile(intermediate_file, fps=24, preset='ultrafast', threads=4)

# [FFmpeg command and execution code follows, unchanged from the previous correction]