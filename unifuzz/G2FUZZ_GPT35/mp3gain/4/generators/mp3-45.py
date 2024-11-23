import os
from pydub import AudioSegment
from pydub.generators import Sine

# Create a directory to save the generated MP3 files
os.makedirs('./tmp/', exist_ok=True)

# Generate multiple audio segments
audio1 = AudioSegment.silent(duration=3000)  # 3 seconds of silent audio
audio2 = Sine(440).to_audio_segment(duration=2000)  # 2 seconds of a sine wave at 440 Hz

# Combine the audio segments
combined_audio = audio1 + audio2

# Export the combined audio to an mp3 file with a specific naming convention
file_name = os.path.join('./tmp/', 'streaming_support_audio.mp3')
combined_audio.export(file_name, format='mp3', bitrate='256k', codec='libmp3lame')

print("Generated 'mp3' file with streaming support audio successfully.")