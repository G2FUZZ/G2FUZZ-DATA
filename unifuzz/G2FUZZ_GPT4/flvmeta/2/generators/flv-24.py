import os
from moviepy.editor import ColorClip, concatenate_videoclips
from moviepy.audio.AudioClip import AudioArrayClip
import numpy as np

# Create the tmp/ directory if it does not exist
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define the path for the output FLV file
flv_file_path = os.path.join(output_dir, "sample_with_vbr_and_sync_tags.flv")

# Create a simple color clip, here a 5-second red clip in 640x480.
color_clip = ColorClip(size=(640, 480), color=(255, 0, 0), duration=5)

# Generate a silent audio clip to match the video duration
# This creates a 5-second silent audio clip with the same fps as the intended audio file
duration = 5  # duration of the audio clip in seconds
fps = 44100  # frames per second
silent_audio = np.zeros((int(duration * fps), 2))  # generate silence, 2 channels for stereo
audio_clip = AudioArrayClip(silent_audio, fps=fps)

color_clip = color_clip.set_audio(audio_clip)

# Write the clip to a .flv file with Variable Bitrate (VBR) Support and Synchronization Tags
# Including the necessary ffmpeg parameters to handle FLV encoding as well as synchronization tags.
color_clip.write_videofile(flv_file_path, codec="libx264", fps=24,
                            ffmpeg_params=["-crf", "23", "-preset", "medium", "-bufsize", "2000k",
                                           "-maxrate", "1500k", "-minrate", "500k", "-ar", "44100"])