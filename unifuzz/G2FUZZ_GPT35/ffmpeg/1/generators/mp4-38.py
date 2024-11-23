import moviepy.editor as mp

# Provide the full path to the input video file
video_path = "full/path/to/input.mp4"
image_path = "full/path/to/image.jpg"

try:
    # Create a VideoClip object
    video = mp.VideoFileClip(video_path)

    # Add subtitles to the video
    subtitles = mp.TextClip("Hello, World!", fontsize=24, color='white').set_position(('center', 'bottom')).set_duration(video.duration)

    video_with_subtitles = mp.CompositeVideoClip([video, subtitles])

    # Load the image to be included in the video
    image = mp.ImageClip(image_path).set_duration(video.duration).resize(height=100).set_position(('center', 'top'))

    # Composite the image with the video
    final_video = mp.CompositeVideoClip([video_with_subtitles, image])

    # Add HDR (High Dynamic Range) effect to the final video
    hdr_clip = final_video.fx(mp.vfx.colorx, 1.2)  # Enhance color and contrast for HDR effect

    # Add Virtual Reality (VR) Support by adding VR content for playback on VR devices
    vr_content = mp.VideoFileClip("full/path/to/vr_content.mp4").set_duration(video.duration)
    final_video_with_vr = mp.CompositeVideoClip([hdr_clip, vr_content])

    # Save the final video with subtitles, image, HDR effect, and VR support
    final_video_with_vr.write_videofile("./tmp/final_video_hdr_vr.mp4", codec="libx264")
except OSError as e:
    print(f"Error: {e}")