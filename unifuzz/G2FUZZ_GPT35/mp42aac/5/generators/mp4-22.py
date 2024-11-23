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

    # Add Timecodes to the video clip
    timecodes = [{'start': 0, 'end': 10, 'timecode_info': 'Timecode Information'}]

    for timecode in timecodes:
        video_clip = video_clip.subclip(timecode['start'], timecode['end']).\
            set_pos(('center', 'top')).\
            set_duration(timecode['end'] - timecode['start']).\
            txt(timecode['timecode_info'], fontsize=18, color='red')
    
    # Add 360-Degree Video feature
    video_clip = video_clip.fx(mp.vfx.mirror_x)

    # Add Digital Watermarking
    watermark_text = "Digital Watermarking: Protect Your Content"
    video_clip = video_clip.set_duration(video_clip.duration).\
        txt(watermark_text, fontsize=18, color='blue', bg_color='white').\
        set_pos(('right', 'bottom'))

    # Write the video with subtitles, timecodes, 360-Degree Video, and Digital Watermarking to a new file
    video_clip.write_videofile("./tmp/video_with_subtitles_timecodes_360degree_and_watermark.mp4", codec="libx264")