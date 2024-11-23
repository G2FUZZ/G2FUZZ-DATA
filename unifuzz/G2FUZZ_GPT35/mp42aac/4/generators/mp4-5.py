import os
from moviepy.editor import VideoFileClip

# Provide the correct path to the input video file
input_video_path = "correct_path_to_input_video.mp4"

# Check if the file exists at the specified location
if os.path.exists(input_video_path):
    # Create a video clip with the correct path
    clip = VideoFileClip(input_video_path)

    # Add metadata to the video clip
    clip = clip.set_audio_metadata(title="Sample Title", artist="Sample Artist", album="Sample Album")

    # Save the modified clip with metadata to a new file
    output_path = "./tmp/sample_output.mp4"
    clip.write_videofile(output_path)
else:
    print(f"Error: The file '{input_video_path}' could not be found.")