import os
from moviepy.editor import ColorClip, concatenate_videoclips, CompositeVideoClip, AudioFileClip
from moviepy.video.fx.all import fadein, fadeout

# Ensure the tmp directory exists
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Specify the output file path
output_file = os.path.join(output_dir, "complex_example.flv")

# Create two simple color clips as example videos
clip1 = ColorClip(size=(640, 480), color=(255, 0, 0), duration=5).set_fps(24)
clip2 = ColorClip(size=(640, 480), color=(0, 0, 255), duration=5).set_fps(24)

# Add fade-in to clip2 and fade-out to clip1 (1 second each)
clip1 = fadeout(clip1, 1)
clip2 = fadein(clip2, 1)

# Create a crossfade transition between clip1 and clip2
transition_duration = 1  # 1 second
clips = [clip1, clip2.crossfadein(transition_duration)]
video = concatenate_videoclips(clips, method="compose", padding=-transition_duration)

# Assuming you have an audio file to add to the video
# Add an audio track to the video
try:
    audio_background = AudioFileClip("background_audio.mp3").subclip(0, video.duration)  # Adjust path as necessary
    video = video.set_audio(audio_background)
except Exception as e:
    print(f"Error adding audio: {e}")

# Write the video file in FLV format
video.write_videofile(output_file, codec="flv")

# Release resources
video.close()