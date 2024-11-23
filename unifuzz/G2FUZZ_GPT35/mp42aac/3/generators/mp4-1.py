# Import necessary libraries
import moviepy.editor as mp

# Create a VideoClip object with a black screen for 5 seconds
clip = mp.ColorClip(size=(640, 480), color=(0, 0, 0), duration=5)

# Set the frames per second (fps) for the video clip
clip = clip.set_fps(24)

# Write the video clip to a file in MP4 format
clip.write_videofile("./tmp/generated_video.mp4", codec="libx264")