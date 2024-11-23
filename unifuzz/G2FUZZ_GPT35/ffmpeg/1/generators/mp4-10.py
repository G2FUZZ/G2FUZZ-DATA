import moviepy.editor as mp

# Create a video clip with a black screen
clip = mp.VideoClip(lambda t: mp.ColorClip(size=(640, 480), color=(0, 0, 0)).get_frame(t), duration=5)

# Write the video clip to an mp4 file
clip.write_videofile("./tmp/editable_video.mp4", codec='libx264', fps=24)