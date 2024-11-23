import os
from moviepy.editor import ColorClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

def generate_flv_file(duration=10, width=640, height=480, fps=24, output_path="./tmp/sample.flv"):
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Create a sample clip (solid color for simplicity)
    clip = ColorClip(size=(width, height), color=(255, 0, 0), duration=duration).set_fps(fps)
    
    # Generate a temporary mp4 file as an intermediate step
    temp_mp4_path = output_path.replace('.flv', '.mp4')
    clip.write_videofile(temp_mp4_path, codec="libx264", fps=fps)
    
    # Extract the mp4 file to an FLV file, including re-encoding
    ffmpeg_extract_subclip(temp_mp4_path, 0, duration, targetname=output_path)
    
    # Clean up the temporary mp4 file
    os.remove(temp_mp4_path)

# Example usage
generate_flv_file()