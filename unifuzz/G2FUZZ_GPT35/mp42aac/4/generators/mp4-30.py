import os
from moviepy.editor import VideoFileClip, AudioFileClip, CompositeVideoClip, TextClip

# Provide the correct paths to input files
input_video_path = "correct_path_to_input_video.mp4"
background_music_path = "correct_path_to_background_music.mp3"

# Check if the input files exist
if os.path.exists(input_video_path) and os.path.exists(background_music_path):
    # Create video clip from the input video
    video_clip = VideoFileClip(input_video_path)

    # Create audio clip from the background music
    audio_clip = AudioFileClip(background_music_path)

    # Overlay the audio clip onto the video clip
    video_clip = video_clip.set_audio(audio_clip)

    # Add text overlay to the video clip
    txt_clip = TextClip("Custom Text Overlay", fontsize=50, color='white')
    txt_clip = txt_clip.set_position(('center', 'bottom')).set_duration(video_clip.duration)
    video_clip = CompositeVideoClip([video_clip, txt_clip])

    # Apply custom video effects
    video_clip = video_clip.fx(vfx.colorx, 0.5)  # Adjust color intensity

    # Save the modified clip with audio overlay, text overlay, and custom effects to a new file
    output_path = "./tmp/sample_output_complex_features.mp4"
    video_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')
else:
    print(f"Error: One or more input files not found.")