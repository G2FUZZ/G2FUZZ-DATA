from moviepy.editor import ColorClip, concatenate_videoclips
from moviepy.video.fx.all import even_size, speedx
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

# Apply slow motion and fast motion effects
# Slow motion: Reduce the speed of the first clip to half its original speed
slow_motion_clip = speedx(final_clip.subclip(0, 2), factor=0.5)
# Fast motion: Increase the speed of the second clip to double its original speed
fast_motion_clip = speedx(final_clip.subclip(2, 4), factor=2)

# Concatenate the modified clips back with the rest of the video
modified_clips = [slow_motion_clip, fast_motion_clip] + [final_clip.subclip(4, final_clip.duration)]
final_clip_with_effects = concatenate_videoclips(modified_clips)

# Save the video as an FLV file with keyframes and Script Data Objects
output_file = os.path.join(output_dir, 'example_with_motion_effects_and_granular_seek.flv')

final_clip_with_effects.write_videofile(output_file, codec='flv', fps=24)

# Generating multiple bitrates for Adaptive Bitrate Streaming (ABS)
bitrates = ['500k', '1000k', '1500k']  # Define desired bitrates
output_files = []

for bitrate in bitrates:
    # Adjust output filename for different bitrates
    output_filename = output_file.replace('.flv', f'_{bitrate}.flv')
    output_files.append(output_filename)
    # Use ffmpeg to create files with different bitrates
    ffmpeg_command = f"""
    ffmpeg -i {output_file} -b:v {bitrate} -bufsize {bitrate} -minrate {bitrate} -maxrate {bitrate} \
    -codec copy -map 0 -flvflags add_keyframe_index {output_filename}
    """
    print(ffmpeg_command)
    # Note: The ffmpeg commands are printed for demonstration and should be executed in your shell.

# Suggest post-process command with ffmpeg (not executable in this Python script directly):
ffmpeg_command = f"""
ffmpeg -i {output_file} -codec copy -map 0 -flvflags add_keyframe_index {output_file.replace('.flv', '_seekable.flv')}
"""

print(f"Video saved to {output_file} and its variants with different bitrates for ABS.")
print("NOTE: This code saves a video with slow and fast motion effects and prepares it for Adaptive Bitrate Streaming.")
print("To add Granular Seek Functionality and prepare ABS, use the above ffmpeg commands after generating the FLV file:")
print("These ffmpeg commands reprocess the FLV files to adjust bitrates and add keyframe indexes for granular seeking and ABS.")