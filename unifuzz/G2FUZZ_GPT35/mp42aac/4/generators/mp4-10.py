import moviepy.editor as mp

# Create a Solid Color Video Clip
video = mp.ColorClip(size=(640, 480), color=(255, 0, 0), duration=2)  # Red color video clip for 2 seconds

# Set the video bitrate to a variable bitrate value for efficient compression
video.write_videofile("./tmp/variable_bitrate_feature.mp4", codec='libx264', fps=25, bitrate='5000k')

print("MP4 file with the Variable Bitrate feature created successfully.")