import os
import moviepy.editor as mp

# Provide the correct path to the video file
video_file_path = "path_to_video_file.mp4"

# Check if the video file exists at the specified path
if os.path.exists(video_file_path):
    # Create a video clip with audio codec AAC
    audio_clip_aac = mp.VideoFileClip(video_file_path).subclip(0, 5)
    audio_clip_aac.audio.write_audiofile("./tmp/audio_clip_aac.mp4", codec='aac')

    # Create a video clip with audio codec MP3
    audio_clip_mp3 = mp.VideoFileClip(video_file_path).subclip(0, 5)
    audio_clip_mp3.audio.write_audiofile("./tmp/audio_clip_mp3.mp4", codec='libmp3lame')

    # Create a video clip with audio codec AC-3
    audio_clip_ac3 = mp.VideoFileClip(video_file_path).subclip(0, 5)
    audio_clip_ac3.audio.write_audiofile("./tmp/audio_clip_ac3.mp4", codec='ac3')
else:
    print(f"Error: The file {video_file_path} could not be found.")