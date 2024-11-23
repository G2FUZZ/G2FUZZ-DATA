import moviepy.editor as mp

# Create a color clip with a resolution of 640x480 and a solid green color
clip = mp.ColorClip(size=(640, 480), color=(0, 255, 0)).set_duration(5)

# Set the frames per second (fps) for the clip
clip.fps = 24

# Set the video codec to H.264 and save the video file
clip.write_videofile("./tmp/video_h264.mp4", codec='libx264')

# Set the video codec to H.265 (HEVC) and save the video file
clip.write_videofile("./tmp/video_h265.mp4", codec='libx265')

# Set the video codec to VP9 and save the video file
clip.write_videofile("./tmp/video_vp9.mp4", codec='libvpx-vp9')