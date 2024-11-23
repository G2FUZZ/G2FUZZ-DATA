import cv2
import numpy as np

# Define the resolution, video codec, frame rate, and duration
width, height = 1920, 1080
fps = 30
duration_sec = 10
codec = cv2.VideoWriter_fourcc(*'mp4v')  # MP4 codec
output_file = './tmp/generated_video_with_keyframes.mp4'
thumbnail_file = './tmp/thumbnail.jpg'  # File path for the still image capture

# Create a video writer object
video = cv2.VideoWriter(output_file, codec, fps, (width, height))

# Generate a blank image (you can change the color as needed)
# Here, it's set to black using zeros. For other colors, use cv2.cvtColor if needed.
frame = np.zeros((height, width, 3), np.uint8)

# Variable to store whether the thumbnail has been captured
thumbnail_captured = False

# Define key frame intervals (for example, one key frame every second)
key_frame_interval = fps  # one key frame per second

# Fill the video with the blank image for the duration specified, insert key frames, and capture a still image
for i in range(fps * duration_sec):
    # For key frames: modify the frame to make it distinguishable as a key frame
    if i % key_frame_interval == 0:
        # Example modification: create a white border around key frames
        key_frame = cv2.copyMakeBorder(frame, 50, 50, 50, 50, cv2.BORDER_CONSTANT, value=[255, 255, 255])
        video.write(key_frame)
    else:
        video.write(frame)
    
    # Capture a still image from the video
    if not thumbnail_captured:
        cv2.imwrite(thumbnail_file, frame)  # Save the current frame as a still image
        thumbnail_captured = True  # Update the flag

# Release the video writer
video.release()

print("Video generation with key frames and still image capture completed.")