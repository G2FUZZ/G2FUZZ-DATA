from moviepy.editor import (VideoFileClip, AudioFileClip, CompositeVideoClip,
                            concatenate_videoclips, vfx, ColorClip, TextClip)  # Added ColorClip and TextClip
import os

# Ensure the tmp directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define basic properties for the clips
clip_duration = 10  # Extended duration for demonstration
clip_size = (640, 480)
bg_color = (0, 0, 0)
txt_color = 'white'

# Background music
bg_music_path = 'path/to/background/music.mp3'  # Adjust path as necessary

# Create a function to generate a complex video clip with additional features
def create_complex_clip(text, filename, codec="libx264", video_bitrate="800k"):
    # Background clip
    bg_clip = ColorClip(size=clip_size, color=bg_color, duration=clip_duration)
    
    # Text clip
    try:
        txt_clip = TextClip(txt=text, fontsize=24, color=txt_color, size=clip_size)
    except Exception as e:
        print(f"Error creating TextClip: {e}")
        return
    txt_clip = txt_clip.set_duration(clip_duration)
    
    # Picture-in-Picture effect (smaller clip at the bottom right corner)
    pip_clip = txt_clip.copy().resize(0.3)  # 30% of the original size
    pip_clip = pip_clip.set_pos(("right", "bottom")).set_start(2)  # Starts 2s into the video
    
    # Combine the background, text, and PiP clips
    video = CompositeVideoClip([bg_clip, txt_clip, pip_clip], size=clip_size)
    
    # Add background music
    try:
        bg_music = AudioFileClip(bg_music_path).subclip(0, clip_duration)  # Match clip's duration
        video = video.set_audio(bg_music)
    except Exception as e:
        print(f"Error adding background music: {e}")
    
    # Add fade-in and fade-out effects
    video = video.fadein(1).fadeout(1)
    
    # Write the result to a file using the specified codec and video bitrate
    video.write_videofile(filename, fps=24, codec=codec, bitrate=video_bitrate)

# Example usage
create_complex_clip("Advanced Features Demo", os.path.join(output_dir, "advanced_features_demo.mp4"))