import moviepy.editor as mp

# Define video parameters
duration = 5  # seconds
resolution = (1280, 720)
fps = 30

# Create a video clip with a solid color for demonstration
clip = mp.ColorClip(size=resolution, color=(0, 0, 255), duration=duration)

# Save the video clip as an mp4 file
clip.write_videofile("./tmp/widely_supported.mp4", fps=fps)