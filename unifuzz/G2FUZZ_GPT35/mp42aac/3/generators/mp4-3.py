import moviepy.editor as mp

# Update the full absolute path to your video file
video_path = "full_absolute_path_to_your_video_file.mp4"

try:
    # Create a VideoClip object
    video = mp.VideoFileClip(video_path)

    # Add subtitles to the video
    subtitles = [{'start': 0, 'end': 3, 'text': 'Subtitle Line 1'},
                 {'start': 3, 'end': 6, 'text': 'Subtitle Line 2'},
                 {'start': 6, 'end': 9, 'text': 'Subtitle Line 3'}]

    subtitles_path = "./tmp/subtitles.srt"

    with open(subtitles_path, "w") as file:
        for i, subtitle in enumerate(subtitles, start=1):
            file.write(f"{i}\n{subtitle['start']} --> {subtitle['end']}\n{subtitle['text']}\n\n")

    # Add the subtitles to the video
    video = video.set_subclip(0, video.duration)
    video = video.set_subtitles(subtitles_path)

    # Save the video with subtitles
    output_path = "./tmp/video_with_subtitles.mp4"
    video.write_videofile(output_path, codec="libx264")

except OSError as e:
    print(f"Error: {e}")