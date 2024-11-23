from moviepy.editor import ColorClip
import subprocess
import os

# Define the properties of the clip
duration = 10  # 10 seconds
width = 640  # Width of the clip
height = 360  # Height of the clip
fps = 24  # Frames per second

# Create a temporary color clip
color_clip = ColorClip(size=(width, height), color=(255, 0, 0), duration=duration)
color_clip = color_clip.set_fps(fps)

# Define the output path for the temporary mp4 file and the final flv file
tmp_mp4_path = './tmp/temp_clip.mp4'
final_flv_path = './tmp/final_clip_vbr.flv'

# Ensure the tmp directory exists
os.makedirs(os.path.dirname(tmp_mp4_path), exist_ok=True)

# Write the color clip to a temporary mp4 file
color_clip.write_videofile(tmp_mp4_path, codec="libx264", audio=False)

# Convert the mp4 file to flv format using ffmpeg command line with flags for seekable stream support
# and variable bitrate (VBR) encoding
subprocess.run(['ffmpeg', '-i', tmp_mp4_path, 
                '-f', 'flv', 
                '-flvflags', 'no_duration_filesize',
                '-vcodec', 'libx264',  # Use libx264 for video encoding
                '-crf', '23',  # CRF for VBR, typical values range from 18 to 28, 23 is default
                '-preset', 'medium',  # Preset for encoding speed to compression ratio
                '-acodec', 'copy',  # Copy the audio stream without re-encoding
                final_flv_path])

# Clean up the temporary mp4 file
os.remove(tmp_mp4_path)

print(f"FLV file with Variable Bitrate (VBR) Encoding and Seekable Stream Support has been saved to {final_flv_path}")