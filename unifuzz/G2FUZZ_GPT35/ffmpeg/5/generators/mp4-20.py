# Importing necessary libraries
import moviepy.editor as mp
import numpy as np

# Function to generate a white color frame
def make_frame(t):
    frame = np.full((480, 640, 3), 255, dtype=np.uint8)  # White color frame
    return frame

# Create a video clip with white color frames
video = mp.VideoClip(make_frame, duration=5)

# Write the video clip to an mp4 file with 3D, Variable Bitrate (VBR)
video.write_videofile("./tmp/generated_3d_vbr_embedded_video.mp4", codec='libx264', fps=24, ffmpeg_params=['-vf', 'stereo3d=sbs2l:abl', '-crf', '23'])