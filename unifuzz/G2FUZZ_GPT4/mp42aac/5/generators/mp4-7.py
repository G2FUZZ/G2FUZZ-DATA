from moviepy.editor import ColorClip

# Parameters for the video
duration = 10  # Duration in seconds
resolution = (1920, 1080)  # Resolution in pixels
color = (255, 0, 0)  # Red color

# Create a color clip without specifying fps here
clip = ColorClip(size=resolution, color=color, duration=duration)

# Define the output path
output_path = './tmp/sample_video.mp4'

# Specify fps when writing the video file
clip.write_videofile(output_path, fps=24, codec='libx264')

print(f"Video saved to {output_path}")