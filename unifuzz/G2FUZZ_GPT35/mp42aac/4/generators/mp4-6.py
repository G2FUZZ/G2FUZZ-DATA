import moviepy.editor as mp

# Create a VideoClip with a black screen
clip = mp.ColorClip((640, 480), color=(0, 0, 0), duration=5)

# Set the audio to None
clip = clip.set_audio(None)

# Write the clip to an mp4 file
clip.write_videofile("./tmp/compatibility.mp4", codec="libx264", fps=24)