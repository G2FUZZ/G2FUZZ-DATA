import os
from moviepy.editor import ColorClip

# Create the tmp/ directory if it does not exist
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define the path for the output FLV file
flv_file_path = os.path.join(output_dir, "sample_with_vbr_support.flv")

# Create a simple color clip, here a 5-second red clip in 640x480.
color_clip = ColorClip(size=(640, 480), color=(255, 0, 0), duration=5)

# Write the clip to a .flv file with Variable Bitrate (VBR) Support
# Note: While MoviePy itself may not explicitly allow setting VBR directly in the API,
# the output parameters can be adjusted to use ffmpeg's VBR settings under the hood.
# The `bitrate` parameter is not directly used here, as ffmpeg's codec options will handle VBR.
# For demonstration purposes, we'll set a nominal target bitrate and specify a quality range,
# which is a common approach for enabling VBR in ffmpeg.
# Example: `-q:v` for video quality scale (lower means better), which indirectly controls the bitrate.

# It's important to note that FLV format and VBR support might have limitations or specific settings needed.
# This example prioritizes the demonstration of how to set variable bitrate settings conceptually.

color_clip.write_videofile(flv_file_path, codec="libx264", fps=24, audio=False,
                            ffmpeg_params=["-crf", "23", "-preset", "medium", "-bufsize", "2000k", "-maxrate", "1500k", "-minrate", "500k"])

# Note: 
# - `-crf` (Constant Rate Factor) affects the quality, lower values mean better quality. Around 18 to 24 is a good range for VBR.
# - `-preset` specifies the encoding speed to compression ratio trade-off (faster encoding with less compression vs. slower encoding with more compression).
# - `-bufsize` specifies the rate control buffer size.
# - `-maxrate` and `-minrate` specify the maximum and minimum bitrate for VBR, enabling ffmpeg to adjust the bitrate dynamically within this range.
# This setup is a basic example and might need adjustments based on specific requirements for FLV files or the target environment.