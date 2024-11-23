from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
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

    # Add Watermarking
    watermark_text = "Copyright © 2022 Your Company"
    txt_clip = TextClip(watermark_text, fontsize=24, color='white', bg_color='black').set_position(('bottom', 'right')).set_duration(clip.duration)
    watermarked_clip = CompositeVideoClip([clip, txt_clip])

    # Save the file with metadata and watermark
    output_path = "./tmp/sample_video_with_metadata_and_watermark.mp4"
    watermarked_clip.write_videofile(output_path, codec="libx264", fps=24)

    print(f"Video file with metadata and watermark saved at: {output_path}")