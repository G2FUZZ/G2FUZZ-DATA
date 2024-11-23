import os
import moviepy.editor as mp

# Provide the correct path to the video file
video_path = "actual_path_to_video_file.mp4"

# Check if the file exists before creating the video clip
if os.path.exists(video_path):
    # Create a video clip object
    clip = mp.VideoFileClip(video_path)

    # Set the video clip's streaming capabilities to Yes
    clip = clip.set(7, True)

    # Set the video clip's 3D video support feature
    clip = clip.set(5, "Capable of storing stereoscopic 3D videos")

    # Set the video clip's Error resilience feature
    clip = clip.set(8, "Includes features to recover from errors in the file structure for improved playback")

    # Save the modified clip with streaming capabilities, 3D video support, and Error resilience to a new file
    clip.write_videofile("./tmp/streaming_3D_video_with_error_resilience.mp4", codec="libx264")
else:
    print(f"Error: File '{video_path}' not found.")