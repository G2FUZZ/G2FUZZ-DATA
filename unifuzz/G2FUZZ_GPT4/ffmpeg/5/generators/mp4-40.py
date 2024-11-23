import cv2
import numpy as np
import moviepy.editor as mp

# Define the resolution, video codec, frame rate, and duration
width, height = 1920, 1080
fps = 30
total_frames = fps * 10  # 10 seconds of video
codec = cv2.VideoWriter_fourcc(*'mp4v')  # MP4 codec
output_file = './tmp/generated_video.mp4'
thumbnail_file = './tmp/thumbnail.jpg'  # File path for the still image capture
edited_video_file = './tmp/edited_video.mp4'  # File path for the edited video

# Create a video writer object
video = cv2.VideoWriter(output_file, codec, fps, (width, height))

# Generate a blank image (you can change the color as needed)
frame = np.zeros((height, width, 3), np.uint8)

# Variable to store whether the thumbnail has been captured
thumbnail_captured = False

# Fill the video with the blank image for the duration specified and capture a still image
for i in range(total_frames):
    video.write(frame)
    
    # Capture a still image from the video
    if not thumbnail_captured:
        cv2.imwrite(thumbnail_file, frame)  # Save the current frame as a still image
        thumbnail_captured = True  # Update the flag

# Release the video writer
video.release()

# Edit video using MoviePy to demonstrate the "Edit Lists" feature
# Load the generated video
clip = mp.VideoFileClip(output_file)

# Example edit list operations:
# 1. Cut the clip from 3 to 7 seconds (skipping certain sections)
cut_clip = clip.subclip(3, 7)
# 2. Concatenate the clip with itself (repeating parts of the video)
final_clip = mp.concatenate_videoclips([cut_clip, cut_clip])

# Write the edited clip to a new file
final_clip.write_videofile(edited_video_file, codec='libx264', fps=fps)

print("Video generation, still image capture, and edit list processing completed.")