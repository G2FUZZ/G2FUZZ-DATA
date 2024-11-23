import os
from pydub import AudioSegment
from pydub.generators import Square

# Create a directory if it does not exist
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample mp3 file with more complex file features
audio_segment_1 = Square(660).to_audio_segment(duration=2000)  # Generate a square wave audio segment at 660 Hz

# Apply effects to the audio segment
custom_audio = audio_segment_1.fade_in(300).fade_out(300)  # Apply fade-in and fade-out effects
custom_audio = custom_audio.set_channels(2)  # Set to stereo
custom_audio = custom_audio.set_frame_rate(44100)  # Set frame rate
custom_audio.export('./tmp/sample_complex_extended_custom.mp3', format="mp3", codec="libmp3lame", bitrate="320k")

print("Generated extended custom complex mp3 file.")