import os
from pydub import AudioSegment

# Create a stereo audio file
stereo_audio = AudioSegment.silent(duration=1000)  # 1 second of silence
stereo_audio = stereo_audio.set_channels(2)  # set to stereo
stereo_audio.export("./tmp/stereo_audio.mp3", format="mp3")

# Create a mono audio file
mono_audio = AudioSegment.silent(duration=1000)  # 1 second of silence
mono_audio = mono_audio.set_channels(1)  # set to mono
mono_audio.export("./tmp/mono_audio.mp3", format="mp3")

print("MP3 files generated successfully.")