import moviepy.editor as mp

# Create a Solid Color Video Clip
video = mp.ColorClip(size=(640, 480), color=(255, 0, 0), duration=2)  # Red color video clip for 2 seconds
video.write_videofile("./tmp/feature.mp4", codec='libx264', fps=25)

print("MP4 file with the feature created successfully.")