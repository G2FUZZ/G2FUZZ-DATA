import moviepy.editor as mp

# Create an audio clip with a sample frequency of 44100 Hz
audio_clip = mp.AudioClip(make_frame=lambda t: [0], duration=5, fps=44100)

# Save the audio clip as an MP4 file with AAC codec
audio_clip.write_audiofile("./tmp/audio_with_aac.mp4", codec='aac')

# Save the audio clip as an MP4 file with MP3 codec
audio_clip.write_audiofile("./tmp/audio_with_mp3.mp4", codec='mp3')

# Save the audio clip as an MP4 file with AC-3 codec
audio_clip.write_audiofile("./tmp/audio_with_ac3.mp4", codec='ac3')

print("MP4 files with different audio codecs have been generated.")