from moviepy.editor import VideoFileClip
import os

# Get the current working directory
current_dir = os.getcwd()

# Specify the relative path to the video file from the current directory
video_relative_path = "relative/path/to/video/video.mp4"

# Construct the full path to the video file
video_path = os.path.join(current_dir, video_relative_path)

# Check if the file exists at the specified path
if os.path.exists(video_path):
    # Create a VideoFileClip object
    clip = VideoFileClip(video_path)

    # Set metadata for the video clip
    clip = clip.set_audio_metadata(title="My Video", artist="John Doe", album="Cool Album")

    # Save the modified video clip with metadata to the specified directory
    clip.write_videofile("./tmp/video_with_metadata.mp4")
else:
    print(f"Error: The file {video_path} could not be found.")