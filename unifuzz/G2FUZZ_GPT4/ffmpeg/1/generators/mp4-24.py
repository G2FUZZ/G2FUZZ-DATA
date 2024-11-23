import os
from moviepy.editor import *
from PIL import Image, ImageDraw
import numpy as np

# Ensure the tmp directory exists
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def circle(radius, color):
    """Create an ImageClip of a circle with the given radius and color."""
    # Create a transparent image
    image_size = (radius * 2, radius * 2)
    image = Image.new("RGBA", image_size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    
    # Draw a circle
    draw.ellipse((0, 0, radius * 2, radius * 2), fill=color)
    
    # Convert PIL image to numpy array
    np_image = np.array(image)
    
    # Create an ImageClip
    return ImageClip(np_image)

def make_moving_circle_clip(duration=10, audio_path=None, loop=False):
    # Create a color clip as a background
    color_clip = ColorClip(size=(640, 480), color=(255, 255, 255), duration=duration)
    
    # Function to position the circle, making it move across the screen
    def position_circle(t):
        """Function that positions the circle across the screen over time"""
        # Circle will move from left to right
        x = int(60 + t * (640 - 120) / duration)  # 60 is starting position, 640-120 is end position
        y = 240  # Middle of the height (480 / 2)
        return x, y
    
    # Create a moving circle using the position_circle function for its position
    moving_circle = circle(radius=50, color=(255, 0, 0)).set_position(position_circle).set_duration(duration)
    
    # Overlay the moving circle on the color clip
    video = CompositeVideoClip([color_clip, moving_circle])

    # If an audio path is provided, first check if the file exists
    if audio_path and os.path.exists(audio_path):
        audio_clip = AudioFileClip(audio_path)
        video = video.set_audio(audio_clip)
    elif audio_path:
        raise FileNotFoundError(f"The specified audio file was not found: {audio_path}")
    
    # Loop the video if requested
    if loop:
        video = video.loop(duration=None)
    
    return video

# Generate the clip and write it to an mp4 file
# Update this path to the correct location of your ALAC (.m4a) audio file
audio_path = 'path/to/your/lossless_audio.m4a'  # Placeholder path; replace with actual path to your ALAC file
try:
    clip = make_moving_circle_clip(duration=10, audio_path=audio_path, loop=True)
    output_path = os.path.join(output_dir, "streaming_example_with_custom_playback.mp4")
    clip.write_videofile(output_path, fps=24, codec='libx264', audio_codec='aac')

    print(f"Video saved to {output_path}")
except FileNotFoundError as e:
    print(e)