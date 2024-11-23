import os

# Define the path for the temporary video file
temp_video_path = './tmp/output_complex.avi'

# Optionally, delete the temporary AVI file if it exists
if os.path.exists(temp_video_path):
    os.remove(temp_video_path)

# Define the path for the MP4 video file
mp4_video_path = './tmp/output_complex_with_music.mp4'

# Check if the MP4 file exists before attempting to delete it
if os.path.exists(mp4_video_path):
    os.remove(mp4_video_path)