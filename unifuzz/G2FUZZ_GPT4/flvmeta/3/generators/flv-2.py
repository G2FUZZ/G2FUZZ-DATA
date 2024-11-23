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

# Define the output paths for Sorenson Spark (H.263) and VP6
# Note: moviepy uses ffmpeg and selects the codec based on the file extension and given parameters.
# Moviepy does not provide direct control over the specific codec variant (e.g., Sorenson Spark) beyond format specification.
# FLV is a container format that can use different codecs, but modern encoding options are more limited.
output_path_spark = os.path.join(output_dir, "video_spark.flv")
output_path_vp6 = os.path.join(output_dir, "video_vp6.flv")

# Write the video file to the disk using the FLV format
# Note: The codec selection for FLV in moviepy/ffmpeg might not directly allow choosing between Sorenson Spark and VP6,
# as this functionality is highly dependent on the version and compile options of the underlying ffmpeg.
clip.write_videofile(output_path_spark, codec='flv', bitrate="2000k")
clip.write_videofile(output_path_vp6, codec='flv', bitrate="2000k")

print(f"Videos saved as {output_path_spark} and {output_path_vp6}")