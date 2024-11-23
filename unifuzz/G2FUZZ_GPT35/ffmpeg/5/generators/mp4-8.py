import moviepy.editor as mp
import numpy as np

# Create a video clip with a black screen for 5 seconds
clip = mp.VideoClip(make_frame=lambda t: np.zeros((720, 1280, 3), dtype=np.uint8), duration=5)

# Set the video clip's audio to None
clip = clip.set_audio(None)

# Set additional metadata for streaming support
clip.write_videofile("./tmp/blank_video_streaming.mp4", codec="libx264", fps=24, preset='ultrafast', ffmpeg_params=['-movflags', 'frag_keyframe+empty_moov'])
