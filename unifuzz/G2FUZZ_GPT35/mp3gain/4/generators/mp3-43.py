import os
from pydub import AudioSegment
from pydub.generators import Square, Sine

# Create a directory to store the generated mp3 files
os.makedirs('./tmp/', exist_ok=True)

# Generate multiple audio segments with different frequencies and durations
audio1 = Sine(440).to_audio_segment(duration=3000)  # 3 seconds of a sine wave at 440 Hz
audio2 = Square(880).to_audio_segment(duration=2000)  # 2 seconds of a square wave at 880 Hz

# Apply fade in/out effects with different durations to the audio segments
fade_in_duration_audio1 = 1000  # 1 second fade in for audio1
fade_out_duration_audio1 = 500  # 0.5 seconds fade out for audio1
fade_in_duration_audio2 = 500  # 0.5 seconds fade in for audio2
fade_out_duration_audio2 = 1000  # 1 second fade out for audio2
audio1 = audio1.fade_in(fade_in_duration_audio1).fade_out(fade_out_duration_audio1)
audio2 = audio2.fade_in(fade_in_duration_audio2).fade_out(fade_out_duration_audio2)

# Combine the audio segments into multiple tracks
audio_track1 = audio1 + audio2
audio_track2 = audio2 + audio1

# Add custom metadata to the audio tracks
audio_track1 = audio_track1.set_sample_width(2).set_frame_rate(44100).set_channels(2)
audio_track2 = audio_track2.set_sample_width(2).set_frame_rate(44100).set_channels(2)

# Export the audio tracks to a single mp3 file with a specific naming convention
file_name = os.path.join('./tmp/', 'complex_multi_track_audio.mp3')
combined_audio = audio_track1.append(audio_track2, crossfade=500)
combined_audio.export(file_name, format='mp3', bitrate='320k', codec='libmp3lame')

print("Generated 'mp3' file with complex multi-track audio successfully.")