import os
from moviepy.editor import ColorClip, AudioClip
from moviepy.video.fx.resize import resize

# Ensure the output directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Generate an MP4 file containing a simple color clip
clip = ColorClip(size=(640, 360), color=(255, 0, 0), duration=10)  # A 10-second red clip

# Resize for demonstration, not necessary for the task
clip_resized = resize(clip, width=640)

# Generate a silent audio clip with the same duration as the video clip
silent_audio = AudioClip(lambda t: 0, duration=clip.duration, fps=44100)

# Set the audio of the video clip
clip_resized = clip_resized.set_audio(silent_audio)

# Output file path
output_file = os.path.join(output_dir, 'mpeg2_in_mp4_example_with_aac_audio.mp4')

# Write the clip to an MP4 file using AAC audio codec
clip_resized.write_videofile(output_file, codec='libx264', audio_codec='aac', fps=24)

print(f"MP4 file with AAC Audio has been generated and saved to {output_file}")