import os
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

# Provide the correct path to the input video file
input_video_path = "correct_path_to_input_video.mp4"

# Check if the file exists at the specified location
if os.path.exists(input_video_path):
    # Create a video clip with the correct path
    video_clip = VideoFileClip(input_video_path)

    # Add metadata to the video clip
    video_clip = video_clip.set_audio_metadata(title="Sample Title", artist="Sample Artist", album="Sample Album")

    # Create a TextClip for subtitles
    subtitles = TextClip("This is a sample subtitle", fontsize=24, color='white').set_position(('center', 'bottom')).set_duration(video_clip.duration)

    # Combine the video clip and subtitles
    final_clip = CompositeVideoClip([video_clip, subtitles])

    # Add digital signature to the final clip
    final_clip = final_clip.set_audio_metadata(digital_signature="Sample Digital Signature")

    # Save the modified clip with subtitles and digital signature to a new file
    output_path = "./tmp/sample_output_with_subtitles_digital_signatures_and_streaming.mp4"
    final_clip.write_videofile(output_path, codec='libx264', method='http_streaming')
else:
    print(f"Error: The file '{input_video_path}' could not be found.")