from pydub import AudioSegment
from pydub.generators import Sine

# Create a custom bitrate stereo audio file with multiple segments concatenated
audio_segment_1 = AudioSegment.silent(duration=500)  # 0.5 seconds of silence

# Create a sample audio segment (sine wave) for demonstration
sample_audio_segment = Sine(440).to_audio_segment(duration=1000)  # 1 second sine wave at 440 Hz
sample_audio_segment.export("sample_audio.wav", format="wav")

audio_segment_2 = AudioSegment.from_file("sample_audio.wav")  # load the created sample audio file

custom_bitrate_audio = audio_segment_1 + audio_segment_2
custom_bitrate_audio = custom_bitrate_audio.set_channels(2)  # set to stereo
custom_bitrate_audio = custom_bitrate_audio.set_frame_rate(44100)  # set frame rate
custom_bitrate_audio.export("./tmp/custom_bitrate_audio.mp3", format="mp3", codec="libmp3lame", bitrate="256k")

print("MP3 file with custom bitrate and multiple segments generated successfully.")