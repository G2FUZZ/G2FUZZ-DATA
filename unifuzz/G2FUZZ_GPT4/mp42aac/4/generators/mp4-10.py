from moviepy.editor import ColorClip, TextClip, concatenate_videoclips
import os

# Ensure the tmp directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define basic properties for the clips
clip_duration = 5
clip_size = (640, 480)
bg_color = (0, 0, 0)
txt_color = 'white'

# Create a function to generate a simple video clip with text
def create_clip(text, filename):
    # Background clip
    bg_clip = ColorClip(size=clip_size, color=bg_color, duration=clip_duration)
    
    # Text clip
    try:
        txt_clip = TextClip(txt=text, fontsize=24, color=txt_color, size=clip_size)
    except Exception as e:
        print(f"Error creating TextClip: {e}")
        return
    txt_clip = txt_clip.set_duration(clip_duration)
    
    # Combine the background and text clips
    video = concatenate_videoclips([bg_clip, txt_clip], method="compose")
    
    # Write the result to a file
    video.write_videofile(filename, fps=24)

# Simulate an interactive menu system
create_clip("Main Menu: Select Option", os.path.join(output_dir, "main_menu.mp4"))
create_clip("Option 1 Content", os.path.join(output_dir, "option_1.mp4"))
create_clip("Option 2 Content", os.path.join(output_dir, "option_2.mp4"))