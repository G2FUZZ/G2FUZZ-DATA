import moviepy.editor as mp

# Create a color clip with a duration of 5 seconds and a resolution of 640x480 with green color
clip = mp.ColorClip(size=(640, 480), color=(0, 255, 0), duration=5)
clip.fps = 30  # Set the frames per second (fps) for the video clip

# Set the video codec to H.264
clip.write_videofile("./tmp/example_video_H264.mp4", codec="libx264")

# Set the video codec to H.265
clip.write_videofile("./tmp/example_video_H265.mp4", codec="libx265")