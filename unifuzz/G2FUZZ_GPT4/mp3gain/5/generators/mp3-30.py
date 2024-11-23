import numpy as np
from pydub import AudioSegment
from pydub.generators import Sine
import os

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate a 1-second sine wave for left and right channels
# Frequency of 440 Hz for the left channel and 442 Hz for the right channel
left_channel = Sine(440).to_audio_segment(duration=1000)
right_channel = Sine(442).to_audio_segment(duration=1000)

# Convert the mono audio segments to numpy arrays
left_channel_array = np.array(left_channel.get_array_of_samples())
right_channel_array = np.array(right_channel.get_array_of_samples())

# Combine the two channels to create a stereo signal
stereo_sound = AudioSegment.from_mono_audiosegments(left_channel, right_channel)

# Export with joint stereo and lowpass filter settings
# Note: Like joint_stereo, the lowpass filter parameter is illustrative and does not exist in pydub's current API.
# To apply a lowpass filter, you would need to ensure the encoder supports it and configure it appropriately.
# The "-af" parameter is used to specify audio filters with ffmpeg, including lowpass.
# Here, "lowpass=f=15000" sets the lowpass filter cutoff frequency to 15kHz, adjust this value as needed.
stereo_sound.export('./tmp/joint_stereo_example_with_technique_and_lowpass.mp3', format='mp3', parameters=["-joint_stereo", "1", "-af", "lowpass=f=15000"])

print("Joint stereo MP3 file with Joint Stereo Encoding Techniques and Lowpass Filter Settings has been generated at './tmp/joint_stereo_example_with_technique_and_lowpass.mp3'")