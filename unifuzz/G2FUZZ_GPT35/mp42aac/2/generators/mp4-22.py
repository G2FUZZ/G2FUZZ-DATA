import numpy as np
import moviepy.editor as mp

def make_frame(t):
    return np.zeros((1080, 1920, 3), dtype=np.uint8)

clip = mp.VideoClip(make_frame, duration=1)
clip.fps = 24  # Set the frames per second
clip.write_videofile("./tmp/high_definition_video_with_timecode.mp4", codec="libx264", audio_codec="aac", bitrate="5M", write_logfile=True, ffmpeg_params=["-timecode", "00:00:00:00"])