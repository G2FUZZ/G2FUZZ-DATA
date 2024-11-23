from moviepy.editor import VideoFileClip
import os

# Provide the correct path to an existing video file
video_file_path = "path_to_existing_video.mp4"

# Check if the video file exists
if not os.path.exists(video_file_path):
    print(f"Error: Video file not found at {video_file_path}")
else:
    # Create a VideoFileClip object
    clip = VideoFileClip(video_file_path)
    clip = clip.set_audio(None)  # Remove audio to create a video only file

    # Set metadata properties including the User Data feature
    clip.reader.metadata['title'] = "Sample Title"
    clip.reader.metadata['artist'] = "Sample Artist"
    clip.reader.metadata['album'] = "Sample Album"
    clip.reader.metadata['genre'] = "Sample Genre"
    clip.reader.metadata['user_data'] = "Custom User Data Here"

    # Save the file with metadata
    output_path = "./tmp/sample_video_with_metadata_and_user_data.mp4"
    clip.write_videofile(output_path, codec="libx264", fps=24)

    print(f"Video file with metadata and User Data saved at: {output_path}")