import os
from pydub import AudioSegment

# Create a stereo audio file with Joint stereo encoding
stereo_audio_joint = AudioSegment.silent(duration=1000)  # 1 second of silence
stereo_audio_joint = stereo_audio_joint.set_channels(2)  # set to stereo
stereo_audio_joint = stereo_audio_joint.set_frame_rate(44100)  # set frame rate
stereo_audio_joint.export("./tmp/stereo_audio_joint.mp3", format="mp3", codec="libmp3lame")

print("MP3 file with Joint stereo encoding generated successfully.")