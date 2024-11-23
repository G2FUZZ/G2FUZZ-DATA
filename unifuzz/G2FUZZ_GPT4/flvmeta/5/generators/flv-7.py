from moviepy.editor import ColorClip

# Define the clip properties
duration = 10  # Duration in seconds
resolution = (640, 480)  # Resolution in pixels
color = (0, 0, 0)  # Black color

# Create a color clip (black)
clip = ColorClip(size=resolution, color=color, duration=duration)

# Set the file path
file_path = './tmp/blank_video.flv'

# Write the clip to an FLV file
clip.write_videofile(file_path, codec="libx264", fps=24)