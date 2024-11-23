import os
from pydub import AudioSegment
from mutagen.id3 import ID3, USLT

# Create a stereo audio file
stereo_audio = AudioSegment.silent(duration=1000)  # 1 second of silence
stereo_audio = stereo_audio.set_channels(2)  # set to stereo
stereo_audio.export("./tmp/stereo_audio.mp3", format="mp3")

# Add lyrics support to the stereo audio file
audio_file = "./tmp/stereo_audio.mp3"
audio = ID3(audio_file)
lyrics = USLT(encoding=3, lang='eng', desc='desc', text='Sample lyrics text')
audio['USLT::eng'] = lyrics
audio.save()

# Create a mono audio file
mono_audio = AudioSegment.silent(duration=1000)  # 1 second of silence
mono_audio = mono_audio.set_channels(1)  # set to mono
mono_audio.export("./tmp/mono_audio.mp3", format="mp3")

# Add lyrics support to the mono audio file
audio_file = "./tmp/mono_audio.mp3"
audio = ID3(audio_file)
lyrics = USLT(encoding=3, lang='eng', desc='desc', text='Sample lyrics text')
audio['USLT::eng'] = lyrics
audio.save()

print("MP3 files with Lyrics support generated successfully.")