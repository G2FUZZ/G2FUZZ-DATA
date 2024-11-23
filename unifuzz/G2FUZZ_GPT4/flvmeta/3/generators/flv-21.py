import os
from moviepy.editor import ColorClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

# Create a temporary video clip
clip = ColorClip(size=(640, 480), color=(255, 0, 0), duration=5)  # 5 seconds of red screen

# Specify the directory and filename for the FLV file
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)
temp_video_path = os.path.join(output_dir, "temp_video.mp4")
flv_video_path = os.path.join(output_dir, "video.flv")

# Write the temporary video clip to a file with H.264 codec
clip.write_videofile(temp_video_path, codec="libx264", fps=24)

# Convert the temporary video to FLV format with H.264 codec, including metadata
# Since ffmpeg_extract_subclip does not allow specifying codecs, we need to use a different approach
# We use ffmpeg directly to convert and ensure H.264 is used
os.system(f'ffmpeg -i {temp_video_path} -c:v libx264 -crf 23 -preset medium -c:a aac -strict experimental {flv_video_path}')

# Clean up the temporary video file
os.remove(temp_video_path)

print(f"FLV video with H.264 Video Codec Support has been saved to: {flv_video_path}")