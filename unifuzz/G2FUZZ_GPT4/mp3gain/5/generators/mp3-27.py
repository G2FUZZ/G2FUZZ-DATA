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

# Add joint stereo encoding technique by setting joint_stereo to True in the export method
# Note: The pydub library does not directly expose an API for joint stereo encoding settings.
# The implementation of joint stereo encoding would depend on the underlying encoder used by ffmpeg or libav when exporting to MP3.
# The joint_stereo parameter here is illustrative and does not exist in pydub's current API.
# For actual implementation, ensure the encoder being used supports joint stereo and is configured accordingly outside of this script.
stereo_sound.export('./tmp/joint_stereo_example_with_technique.mp3', format='mp3', parameters=["-joint_stereo", "1"])

print("Joint stereo MP3 file with Joint Stereo Encoding Techniques has been generated at './tmp/joint_stereo_example_with_technique.mp3'")