import moviepy.editor as mp

# Create a ColorClip with white color
video_clip = mp.ColorClip(size=(640, 480), color=(255, 255, 255), duration=5)

# Set the frames per second (fps) for the video clip
video_clip.fps = 24

# Set video codec to H.264 and audio codec to AAC
video_clip.write_videofile("./tmp/sample_video.mp4", codec="libx264", audio_codec="aac")