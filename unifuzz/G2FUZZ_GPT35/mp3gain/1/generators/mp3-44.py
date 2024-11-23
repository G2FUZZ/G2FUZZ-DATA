import os
from pydub import AudioSegment

# Create a directory if it does not exist
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample mp3 file with more complex audio features
sample_audio_segment = AudioSegment.silent(duration=3000)  # 3 seconds of silence
sample_audio_segment = sample_audio_segment.low_pass_filter(2000)  # Apply low-pass filter
sample_audio_segment = sample_audio_segment.high_pass_filter(500)  # Apply high-pass filter
sample_audio_segment = sample_audio_segment.fade_in(500)  # Apply fade-in effect
sample_audio_segment = sample_audio_segment.fade_out(500)  # Apply fade-out effect
sample_audio_segment = sample_audio_segment.set_channels(2)  # Set to stereo
sample_audio_segment = sample_audio_segment.set_frame_rate(44100)  # Set frame rate
sample_audio_segment.export("./tmp/sample_complex_extended_audio.mp3", format="mp3", codec="libmp3lame", bitrate="320k")

print("Generated extended complex audio mp3 file successfully.")