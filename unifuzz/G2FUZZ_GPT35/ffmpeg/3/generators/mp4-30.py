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

    # Set the video clip's In-band metadata feature
    clip = clip.set(8, "Ability to include metadata within the file itself for easier management")

    # Save the modified clip with streaming capabilities, 3D video support, and In-band metadata to a new file
    clip.write_videofile("./tmp/streaming_3D_metadata_video.mp4", codec="libx264")
else:
    print(f"Error: File '{video_path}' not found.")