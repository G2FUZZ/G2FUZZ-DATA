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
    subtitles = [{'start': 1, 'end': 3, 'text': 'Hello World', 'pos': ('center', 'bottom'), 'fontsize': 24, 'color': 'white'},
                 {'start': 4, 'end': 6, 'text': 'Subtitle Example', 'pos': ('right', 'top'), 'fontsize': 32, 'color': 'red'}]

    video_clip = video_clip.subclip(0, 10)
    for subtitle in subtitles:
        video_clip = video_clip.subclip(subtitle['start'], subtitle['end']).\
            set_pos(subtitle['pos']).\
            set_duration(subtitle['end'] - subtitle['start']).\
            txt(subtitle['text'], fontsize=subtitle['fontsize'], color=subtitle['color'])

    # Add watermark to the video clip
    watermark = mp.TextClip("Watermark", fontsize=50, color='white').\
        set_position(('right', 'bottom')).set_duration(10)
    
    video_clip = mp.CompositeVideoClip([video_clip, watermark])

    # Write the video with subtitles and watermark to a new file
    video_clip.write_videofile("./tmp/video_with_complex_features.mp4", codec="libx264")