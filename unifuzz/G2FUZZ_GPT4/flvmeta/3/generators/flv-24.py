import os
from moviepy.editor import ColorClip, concatenate_videoclips

# Directory to save the generated FLV files
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Video settings
duration = 5  # seconds
resolution = (640, 480)  # width, height
base_fps = 24  # frames per second

# Generate a video using a basic color frame as an example
base_clip = ColorClip(size=resolution, color=(255, 0, 0), duration=duration)
base_clip = base_clip.set_fps(base_fps)

# Define the output paths
output_path_spark = os.path.join(output_dir, "video_spark.flv")
output_path_vp6 = os.path.join(output_dir, "video_vp6.flv")
output_path_vp6_scaling = os.path.join(output_dir, "video_vp6_scaling.flv")
output_path_frame_rate_flexibility = os.path.join(output_dir, "video_frame_rate_flexibility.flv")

# Write the video file to the disk using the FLV format for Sorenson Spark
base_clip.write_videofile(output_path_spark, codec='flv', bitrate="2000k")

# Write the video file to the disk using the FLV format for VP6
base_clip.write_videofile(output_path_vp6, codec='flv', bitrate="2000k")

# For VP6 with scaling feature, we assume here that by specifying a higher bitrate,
# the playback quality can be dynamically adjusted without altering the scale.
base_clip.write_videofile(output_path_vp6_scaling, codec='flv', bitrate="5000k")

# Frame Rate Flexibility: Generate clips with varying frame rates and concatenate them
clip1 = base_clip.set_fps(12)  # Lower frame rate for the first part
clip2 = base_clip.set_fps(24)  # Base frame rate for the second part
clip3 = base_clip.set_fps(48)  # Higher frame rate for the third part

# Concatenate the clips to create a single video with variable frame rates
variable_fps_clip = concatenate_videoclips([clip1, clip2, clip3])

# Write the video file with variable frame rates
variable_fps_clip.write_videofile(output_path_frame_rate_flexibility, codec='flv', bitrate="3000k")

print(f"Videos saved as {output_path_spark}, {output_path_vp6}, {output_path_vp6_scaling}, and {output_path_frame_rate_flexibility}")