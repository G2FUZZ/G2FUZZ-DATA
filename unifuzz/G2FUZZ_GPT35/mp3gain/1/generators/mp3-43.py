import os
from pydub import AudioSegment, generators
from mutagen.id3 import ID3, USLT

# Create a stereo audio file with various effects applied
stereo_audio = AudioSegment.from_file("sample_audio.wav")  # Load the sample audio file

# Apply effects to the stereo audio
stereo_audio_filtered = stereo_audio.low_pass_filter(3000)  # Apply low-pass filter
stereo_audio_faded_in = stereo_audio.fade_in(200)  # Apply fade-in effect
stereo_audio_faded_out = stereo_audio.fade_out(200)  # Apply fade-out effect

# Concatenate the processed audio segments
stereo_audio_custom = stereo_audio_filtered + stereo_audio_faded_in + stereo_audio_faded_out
stereo_audio_custom = stereo_audio_custom.set_channels(2)  # Set to stereo
stereo_audio_custom = stereo_audio_custom.set_frame_rate(44100)  # Set frame rate
stereo_audio_custom.export("./tmp/stereo_custom_audio.mp3", format="mp3")

# Add lyrics support to the stereo audio file
audio_file = "./tmp/stereo_custom_audio.mp3"
audio = ID3(audio_file)
lyrics = USLT(encoding=3, lang='eng', desc='desc', text='Sample lyrics text')
audio['USLT::eng'] = lyrics
audio.save()

# Create a mono audio file with a square wave audio segment
mono_audio = AudioSegment.silent(duration=1000)  # 1 second of silence
mono_audio_square = generators.Square(660).to_audio_segment(duration=1500)  # Generate a square wave audio segment at 660 Hz

# Concatenate the mono audio with the square wave segment
mono_audio_custom = mono_audio + mono_audio_square
mono_audio_custom = mono_audio_custom.set_channels(1)  # Set to mono
mono_audio_custom.export("./tmp/mono_custom_audio.mp3", format="mp3")

# Add lyrics support to the mono audio file
audio_file = "./tmp/mono_custom_audio.mp3"
audio = ID3(audio_file)
lyrics = USLT(encoding=3, lang='eng', desc='desc', text='Sample lyrics text')
audio['USLT::eng'] = lyrics
audio.save()

print("MP3 files with custom features and Lyrics support generated successfully.")