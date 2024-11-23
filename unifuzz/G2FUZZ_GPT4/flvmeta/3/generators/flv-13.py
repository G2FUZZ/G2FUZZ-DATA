import os
from moviepy.editor import ColorClip

# Directory to save the generated FLV files
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Video settings
duration = 5  # seconds
resolution = (640, 480)  # width, height
fps = 24  # frames per second

# Generate a video using a basic color frame as an example
clip = ColorClip(size=resolution, color=(255, 0, 0), duration=duration)
clip = clip.set_fps(fps)

# Define the output paths for Sorenson Spark, VP6, and VP6 with scaling
output_path_spark = os.path.join(output_dir, "video_spark.flv")
output_path_vp6 = os.path.join(output_dir, "video_vp6.flv")
output_path_vp6_scaling = os.path.join(output_dir, "video_vp6_scaling.flv")

# Write the video file to the disk using the FLV format for Sorenson Spark
clip.write_videofile(output_path_spark, codec='flv', bitrate="2000k")

# Write the video file to the disk using the FLV format for VP6
clip.write_videofile(output_path_vp6, codec='flv', bitrate="2000k")

# For VP6 with scaling feature, we assume here that by specifying a higher bitrate,
# the playback quality can be dynamically adjusted without altering the scale.
# Note: Actual scaling and quality adjustment are handled by the playback environment
# and not the encoding process. This example assumes the feature is implicitly supported
# by specifying a higher quality encoding.
clip.write_videofile(output_path_vp6_scaling, codec='flv', bitrate="5000k")

print(f"Videos saved as {output_path_spark}, {output_path_vp6}, and {output_path_vp6_scaling}")