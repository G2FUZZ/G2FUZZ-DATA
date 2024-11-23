import moviepy.editor as mp

# Provide the full path to the input video file
video_path = "full/path/to/input.mp4"

try:
    # Create a VideoClip object with variable frame rate (VFR)
    video = mp.VideoFileClip(video_path)
    video = video.set_fps(30)

    # Add subtitles to the video
    subtitles = mp.TextClip("Hello, World!", fontsize=24, color='white').set_position(('center', 'bottom')).set_duration(video.duration)

    video_with_subtitles = mp.CompositeVideoClip([video, subtitles])

    # Save the video with subtitles and variable frame rate
    video_with_subtitles.write_videofile("./tmp/video_with_subtitles_vfr.mp4", codec="libx264", fps=video.fps, preset='ultrafast')
except OSError as e:
    print(f"Error: {e}")