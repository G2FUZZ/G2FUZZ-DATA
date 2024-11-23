import moviepy.editor as mp

# Define the duration of the video in seconds
duration = 10

# Create a video clip with high-definition video and audio content
clip = mp.VideoClip(lambda t: (mp.ColorClip((1280, 720), color=(0, 0, 0)).get_frame(t)), duration=duration)
clip = clip.set_audio(mp.AudioClip(lambda t: 0, duration=duration).set_duration(duration))

# Write the video clip to an mp4 file
output_path = './tmp/high_definition_video_with_timecodes.mp4'
clip.write_videofile(output_path, codec='libx264', audio_codec='aac', fps=24, bitrate='5000k')

print(f'File saved at: {output_path}')