from moviepy.editor import ColorClip, concatenate_audioclips, AudioClip
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Define the path for the output video file
output_path = os.path.join(output_dir, 'output_video_360_with_low_delay_audio.mp4')

# Create a simple video clip (e.g., 10 seconds of red screen)
clip = ColorClip(size=(640, 480), color=(255, 0, 0), duration=10)

# Generate a silent audio clip matching the duration of the video clip
def make_silent_audio(duration):
    return AudioClip(lambda t: 0, duration=duration, fps=44100)

audio_clip = make_silent_audio(clip.duration)

# Setting the audio of the video clip
clip = clip.set_audio(audio_clip)

# Write the video file with low delay optimized audio
clip.write_videofile(output_path, codec="libx264", audio_codec="aac", fps=24, ffmpeg_params=['-tune', 'zerolatency'])

# Continue with the rest of your code for adding metadata...