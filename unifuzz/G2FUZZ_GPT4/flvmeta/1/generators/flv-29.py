import os
from moviepy.editor import ColorClip

# Create the tmp directory if it doesn't exist
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Parameters for the video
duration = 5  # duration of the video in seconds
resolution = (640, 360)  # resolution of the video
color = (255, 0, 0)  # color of the video in RGB

# Create a color clip
clip = ColorClip(size=resolution, color=color, duration=duration)

# Export the clip as an FLV file with H.264 codec, specifying the fps
# This setup implies the use of NAL units as H.264 inherently uses NAL units for video data representation
# The "Legacy Device Support" feature does not directly translate to a specific ffmpeg parameter, but ensuring broad compatibility
# can include using widely supported options and avoiding high-profile features that may not be supported by older devices.
flv_filename = os.path.join(output_dir, 'legacy_device_support_with_NAL_units.flv')
clip.write_videofile(flv_filename, codec='libx264', fps=24, write_logfile=True, 
                     ffmpeg_params=['-flvflags', 'no_duration_filesize', '-profile:v', 'baseline', '-level', '3.0'])

print(f"FLV file with streaming capabilities, NAL units feature, and Legacy Device Support has been saved to {flv_filename}")