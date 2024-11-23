import moviepy.editor as mp
import numpy as np

def generate_blank_video_with_resolution(video_resolution):
    if video_resolution == 'SD':
        resolution = (640, 480)
    elif video_resolution == 'HD':
        resolution = (1280, 720)
    elif video_resolution == '4K':
        resolution = (3840, 2160)
    else:
        raise ValueError("Unsupported video resolution")

    # Create a video clip with a black screen for 5 seconds and specified resolution
    clip = mp.VideoClip(make_frame=lambda t: np.zeros((resolution[1], resolution[0], 3), dtype=np.uint8), duration=5)

    # Set the video clip's audio to None
    clip = clip.set_audio(None)

    # Set additional metadata for streaming support
    clip.write_videofile(f"./tmp/blank_video_{video_resolution}_streaming.mp4", codec="libx264", fps=24, preset='ultrafast', ffmpeg_params=['-movflags', 'frag_keyframe+empty_moov'])

# Generate a blank video with HD resolution
generate_blank_video_with_resolution('HD')