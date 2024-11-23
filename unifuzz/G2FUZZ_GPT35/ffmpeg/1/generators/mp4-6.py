import moviepy.editor as mp

# Provide the full path to the input video file
video_path = "full/path/to/input.mp4"

try:
    # Create a VideoClip object
    video = mp.VideoFileClip(video_path)

    # Add subtitles to the video
    subtitles = mp.TextClip("Hello, World!", fontsize=24, color='white').set_position(('center', 'bottom')).set_duration(video.duration)

    video_with_subtitles = mp.CompositeVideoClip([video, subtitles])

    # Save the video with subtitles
    video_with_subtitles.write_videofile("./tmp/video_with_subtitles.mp4", codec="libx264")
except OSError as e:
    print(f"Error: {e}")