import moviepy.editor as mp

# Create a blank audio clip with duration 1 second
audio_clip = mp.AudioClip(lambda t: [0], duration=1)

# Set the fps attribute of the audio clip
audio_clip.fps = 44100  # Set the fps to a common value for audio

# Set the audio codec to AAC
audio_clip.write_audiofile("./tmp/audio_aac.mp4", codec='aac')

# Set the audio codec to MP3
audio_clip.write_audiofile("./tmp/audio_mp3.mp4", codec='libmp3lame')