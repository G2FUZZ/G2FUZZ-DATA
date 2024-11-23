import os
from moviepy.editor import ColorClip, concatenate_videoclips, CompositeVideoClip

def generate_complex_flv_file(duration_per_clip=5, width=640, height=480, fps=24, output_path="./tmp/complex_sample.flv"):
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Define colors for the clips
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
    clips = []
    
    for index, color in enumerate(colors):
        # Create a sample clip (solid color)
        clip = ColorClip(size=(width, height), color=color, duration=duration_per_clip).set_fps(fps)
        
        # Normally, you would add a text annotation here, but we're omitting it due to ImageMagick issues
        
        clips.append(clip)
    
    # Concatenate clips with a transition. Here we just concatenate without a fancy transition for simplicity.
    final_clip = concatenate_videoclips(clips, method="compose")
    
    # Generate a temporary mp4 file as an intermediate step
    temp_mp4_path = output_path.replace('.flv', '.mp4')
    final_clip.write_videofile(temp_mp4_path, codec="libx264", fps=fps)
    
    # Note: Directly generating FLV might not be supported with the latest ffmpeg/codec configurations,
    # so it's recommended to stick with more common formats like MP4 if possible.
    # If FLV is absolutely necessary, consider using ffmpeg command line tools to convert the MP4 to FLV.

    # Clean up the temporary mp4 file if no longer needed
    # os.remove(temp_mp4_path)

# Example usage
generate_complex_flv_file()