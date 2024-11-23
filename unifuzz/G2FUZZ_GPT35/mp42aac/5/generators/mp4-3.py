import os
import moviepy.editor as mp

video_file_path = "sample_video.mp4"

# Check if the video file exists
if not os.path.exists(video_file_path):
    print(f"Error: File '{video_file_path}' not found.")
else:
    # Create a VideoClip object
    video_clip = mp.VideoFileClip(video_file_path)

    # Add subtitles to the video clip
    subtitles = [{'start': 1, 'end': 3, 'text': 'Hello World'},
                 {'start': 4, 'end': 6, 'text': 'Subtitle Example'}]

    video_clip = video_clip.subclip(0, 10)
    for subtitle in subtitles:
        video_clip = video_clip.subclip(subtitle['start'], subtitle['end']).\
            set_pos(('center', 'bottom')).\
            set_duration(subtitle['end'] - subtitle['start']).\
            txt(subtitle['text'], fontsize=24, color='white')

    # Write the video with subtitles to a new file
    video_clip.write_videofile("./tmp/video_with_subtitles.mp4", codec="libx264")