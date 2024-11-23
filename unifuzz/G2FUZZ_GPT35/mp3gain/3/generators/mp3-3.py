import os
from pydub import AudioSegment
from pydub.generators import Sine

# Create a stereo mp3 file
stereo_sound = Sine(440).to_audio_segment(duration=1000)
stereo_sound = stereo_sound.pan(-1.0) + stereo_sound.pan(1.0)
stereo_sound.export("./tmp/stereo_sound.mp3", format="mp3")

# Create a mono mp3 file
mono_sound = Sine(440).to_audio_segment(duration=1000)
mono_sound.export("./tmp/mono_sound.mp3", format="mp3")