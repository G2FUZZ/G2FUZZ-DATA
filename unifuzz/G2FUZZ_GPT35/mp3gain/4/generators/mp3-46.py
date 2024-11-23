import os
from pydub import AudioSegment
from pydub.generators import Sine

# Create a directory to store the generated mp3 files
os.makedirs('./tmp/', exist_ok=True)

# Generate multiple audio segments
audio1 = AudioSegment.silent(duration=3000)  # 3 seconds of silent audio
audio2 = Sine(440).to_audio_segment(duration=2000)  # 2 seconds of a sine wave at 440 Hz

# Apply fade in/out effects to the audio segments
fade_in_duration = 500  # 0.5 seconds fade in
fade_out_duration = 500  # 0.5 seconds fade out
audio1 = audio1.fade_in(fade_in_duration).fade_out(fade_out_duration)
audio2 = audio2.fade_in(fade_in_duration).fade_out(fade_out_duration)

# Combine the audio segments
combined_audio = audio1 + audio2

# Add metadata to the combined audio
combined_audio = combined_audio.set_frame_rate(44100).set_channels(2)

# Export the combined audio to an mp3 file with a specific naming convention
file_name = os.path.join('./tmp/', 'complex_file_with_metadata_and_fade_effects.mp3')
combined_audio.export(file_name, format='mp3', bitrate='256k', codec='libmp3lame')

print("Generated 'mp3' file with complex file features successfully.")