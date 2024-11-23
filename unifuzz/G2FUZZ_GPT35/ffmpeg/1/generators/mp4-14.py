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

    # Set metadata properties
    clip.reader.metadata['title'] = "Sample Title"
    clip.reader.metadata['artist'] = "Sample Artist"
    clip.reader.metadata['album'] = "Sample Album"
    clip.reader.metadata['genre'] = "Sample Genre"
    
    # Add 3D Video Support metadata
    clip.reader.metadata['3D_video_support'] = "MP4 files can contain 3D video content for viewing with compatible devices."

    # Save the file with metadata
    output_path = "./tmp/sample_video_with_metadata_and_3D.mp4"
    clip.write_videofile(output_path, codec="libx264", fps=24)

    print(f"Video file with metadata and 3D Video Support saved at: {output_path}")