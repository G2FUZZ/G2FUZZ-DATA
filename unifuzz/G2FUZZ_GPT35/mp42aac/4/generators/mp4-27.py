import os
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, concatenate_videoclips

# Provide the correct path to the input video file
input_video_path = "correct_path_to_input_video.mp4"

# Check if the file exists at the specified location
if os.path.exists(input_video_path):
    # Create a video clip with the correct path
    video_clip = VideoFileClip(input_video_path)

    # Add metadata to the video clip
    video_clip = video_clip.set_audio_metadata(title="Sample Title", artist="Sample Artist", album="Sample Album")

    # Create multiple TextClips for subtitles with different styles and positions
    subtitle1 = TextClip("Subtitle 1", fontsize=36, color='red').set_position(('center', 'top')).set_duration(5)
    subtitle2 = TextClip("Subtitle 2", fontsize=28, color='blue').set_position(('left', 'bottom')).set_duration(7)

    # Concatenate the video clip with multiple subtitles
    final_clip = concatenate_videoclips([video_clip, subtitle1.set_start(5), subtitle2.set_start(10)])

    # Save the modified clip with multiple subtitles to a new file
    output_path = "./tmp/sample_output_with_multiple_subtitles.mp4"
    final_clip.write_videofile(output_path, codec='libx264')
else:
    print(f"Error: The file '{input_video_path}' could not be found.")