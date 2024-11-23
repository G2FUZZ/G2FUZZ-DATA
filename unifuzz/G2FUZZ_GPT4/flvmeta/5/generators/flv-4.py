from moviepy.editor import ColorClip

# Define the parameters for the clip
duration = 10  # Duration in seconds
resolution = (640, 480)  # Resolution of the clip
color = (255, 0, 0)  # Color of the clip in RGB

# Create a color clip
clip = ColorClip(size=resolution, color=color, duration=duration)

# Set the fps for the clip
clip.fps = 24  # Setting fps for the clip

# Specify the output path
output_path = './tmp/sample_video.flv'

# Write the video file in FLV format
clip.write_videofile(output_path, codec='flv')  # fps is already set for the clip