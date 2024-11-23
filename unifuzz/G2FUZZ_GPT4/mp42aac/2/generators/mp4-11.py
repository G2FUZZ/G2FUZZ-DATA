from moviepy.editor import ColorClip
import os

# Ensure the tmp directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Create a simple video clip
clip = ColorClip(size=(640, 360), color=(255, 0, 0), duration=10)  # A 10-second red video

# Set the output file path
output_file = os.path.join(output_dir, 'example_with_vbr.mp4')

# Write the video file to disk with VBR encoding
clip.write_videofile(output_file, codec="libx264", fps=24,
                     bitrate="2000k", audio_bitrate="128k",
                     ffmpeg_params=["-crf", "23", "-preset", "medium", "-profile:v", "high", "-bf", "2", "-coder", "1", "-movflags", "+faststart"])

print(f"Video saved to {output_file}")