import os
import moviepy.editor as mp

# Create a VideoClip with a black screen
clip = mp.ColorClip((640, 480), color=(0, 0, 0), duration=5)

# Set the first audio track
audio_file_1 = "audio_track_1.mp3"
if os.path.exists(audio_file_1):
    audio_clip_1 = mp.AudioFileClip(audio_file_1)
    clip = clip.set_audio(audio_clip_1)
else:
    print(f"Error: File '{audio_file_1}' not found.")

# Set the second audio track
audio_file_2 = "audio_track_2.mp3"
if os.path.exists(audio_file_2):
    audio_clip_2 = mp.AudioFileClip(audio_file_2)
    clip = clip.set_audio(audio_clip_2, apply_to="mask")
else:
    print(f"Error: File '{audio_file_2}' not found.")

# Write the clip to an mp4 file with multiple audio tracks
clip.write_videofile("./tmp/multiple_audio_tracks.mp4", codec="libx264", fps=24, audio_codec="aac")