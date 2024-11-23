import moviepy.editor as mp

# Update the full absolute paths to your video and audio files
video_path_1 = "full_absolute_path_to_video_clip_1.mp4"
video_path_2 = "full_absolute_path_to_video_clip_2.mp4"
audio_path = "full_absolute_path_to_audio_file.mp3"

try:
    # Create VideoClip objects for each video clip
    video_clip_1 = mp.VideoFileClip(video_path_1)
    video_clip_2 = mp.VideoFileClip(video_path_2)

    # Trim the video clips if needed
    video_clip_1 = video_clip_1.subclip(0, 10)  # Trim from 0s to 10s
    video_clip_2 = video_clip_2.subclip(5, 15)  # Trim from 5s to 15s

    # Create an AudioFileClip object for the audio overlay
    audio_clip = mp.AudioFileClip(audio_path)

    # Overlay the audio on the video clips
    video_clip_1 = video_clip_1.set_audio(audio_clip)
    video_clip_2 = video_clip_2.set_audio(audio_clip)

    # Add custom effects to the video clips (e.g., resize, rotate, speed up)
    video_clip_1 = video_clip_1.resize(width=640)  # Resize video clip 1 to width 640
    video_clip_2 = video_clip_2.fx(mp.vfx.speedx, 2)  # Double the speed of video clip 2

    # Concatenate the video clips
    final_clip = mp.concatenate_videoclips([video_clip_1, video_clip_2])

    # Save the final video with custom effects
    output_path = "./tmp/final_video_with_effects.mp4"
    final_clip.write_videofile(output_path, codec="libx264")

except OSError as e:
    print(f"Error: {e}")