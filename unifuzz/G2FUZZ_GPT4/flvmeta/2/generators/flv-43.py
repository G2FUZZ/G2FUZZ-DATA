import os
from moviepy.editor import concatenate_videoclips, ColorClip, AudioFileClip
import subprocess

# Create the tmp/ directory if it does not exist
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define the path for the output FLV file
flv_file_path = os.path.join(output_dir, "complex_sample.flv")

# Create a series of color clips with different colors and durations
clips = [
    ColorClip(size=(640, 480), color=(255, 0, 0), duration=5),
    ColorClip(size=(640, 480), color=(0, 255, 0), duration=3),
    ColorClip(size=(640, 480), color=(0, 0, 255), duration=4)
]

# Combine the color clips into a single video clip
combined_clip = concatenate_videoclips(clips)

# Specify an audio file to add to the video (check if the audio file exists at this path)
audio_file_path = os.path.join(output_dir, "background_audio.mp3")

if os.path.exists(audio_file_path):
    audio_clip = AudioFileClip(audio_file_path)
    # Set the audio of the combined clip
    combined_clip = combined_clip.set_audio(audio_clip)
else:
    print(f"Warning: Audio file not found at {audio_file_path}. Proceeding without audio.")

# Write the combined clip to a temporary MP4 file (easier processing before converting to FLV)
temporary_mp4_path = flv_file_path.replace(".flv", ".mp4")
combined_clip.write_videofile(temporary_mp4_path, codec="libx264", fps=24)

# The rest of your script remains unchanged...