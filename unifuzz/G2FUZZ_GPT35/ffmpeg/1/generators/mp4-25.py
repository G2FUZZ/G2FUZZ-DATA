import moviepy.editor as mp

# Provide the full path to the input video file
video_path = "full/path/to/input.mp4"

try:
    # Create a VideoClip object
    video = mp.VideoFileClip(video_path)

    # Add subtitles to the video
    subtitles = mp.TextClip("Hello, World!", fontsize=24, color='white').set_position(('center', 'bottom')).set_duration(video.duration)

    video_with_subtitles = mp.CompositeVideoClip([video, subtitles])

    # Add Streaming Protocols feature
    hls_feature = mp.vfx.fadein(video_with_subtitles, 1).fadeout(1)
    hls_feature.write_videofile("./tmp/video_with_subtitles_hls.mp4", codec="libx264", method="hls")

    dash_feature = mp.vfx.fadein(video_with_subtitles, 1).fadeout(1)
    dash_feature.write_videofile("./tmp/video_with_subtitles_dash.mp4", codec="libx264", method="dash")

    # Add Scripting Support feature
    scripting_support_feature = video_with_subtitles
    scripting_support_feature.write_videofile("./tmp/video_with_subtitles_scripting.mp4", codec="libx264", method="ffmpeg")

except OSError as e:
    print(f"Error: {e}")