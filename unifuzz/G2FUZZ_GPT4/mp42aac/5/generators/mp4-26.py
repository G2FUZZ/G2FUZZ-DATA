import os
from PIL import Image, ImageDraw
from moviepy.editor import ImageClip
from mutagen.mp4 import MP4

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate a black image using PIL
image_path = './tmp/black_image.png'
img = Image.new('RGB', (640, 360), color='black')
draw = ImageDraw.Draw(img)
draw.text((10, 10), "Sample Video", fill="white")
img.save(image_path)

# Create a video clip from the generated image
clip = ImageClip(image_path)
clip = clip.set_duration(5)  # Set the duration of the video clip to 5 seconds
video_path = './tmp/sample_video.mp4'

# Use 'libx264' codec without specifying 'h263' in ffmpeg_params
clip.write_videofile(video_path, fps=24, codec='libx264')

# Add metadata to the mp4 file
video = MP4(video_path)
video["\xa9nam"] = "Sample Video Title"  # Title
video["\xa9ART"] = "Sample Artist"  # Artist
video["\xa9alb"] = "Sample Album"  # Album
video["\xa9day"] = "2023"  # Year
video["\xa9cmt"] = "Sample comment, description, or any other information."  # Comment

# Save the changes
video.save()

# Cleanup: remove the temporary image file
os.remove(image_path)