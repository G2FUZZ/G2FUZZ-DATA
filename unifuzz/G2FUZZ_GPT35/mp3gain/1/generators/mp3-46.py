from pydub import AudioSegment
from pydub.generators import Sawtooth

# Create multiple audio segments with different effects applied
audio_segment_1 = AudioSegment.from_file("sample_audio.wav")  # Load the sample audio file

# Apply effects to the audio segments
audio_segment_2 = audio_segment_1.low_pass_filter(2000)  # Apply low-pass filter with a different cutoff frequency
audio_segment_3 = audio_segment_1.high_pass_filter(500)  # Apply high-pass filter with a different cutoff frequency
audio_segment_4 = audio_segment_1.fade_in(300)  # Apply fade-in effect with a longer duration
audio_segment_5 = audio_segment_1.fade_out(300)  # Apply fade-out effect with a longer duration
audio_segment_6 = Sawtooth(660).to_audio_segment(duration=1200)  # Generate a sawtooth wave audio segment at 660 Hz

# Concatenate the audio segments
custom_audio = audio_segment_2 + audio_segment_3 + audio_segment_4 + audio_segment_5 + audio_segment_6
custom_audio = custom_audio.set_channels(2)  # Set to stereo
custom_audio = custom_audio.set_frame_rate(44100)  # Set frame rate
custom_audio.export("./tmp/custom_complex_audio.mp3", format="mp3", codec="libmp3lame", bitrate="320k")

print("MP3 file with custom complex features generated successfully.")