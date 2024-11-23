import os
from pydub import AudioSegment
from pydub.generators import Sine
from pydub.playback import play

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate a sine wave tone as an example of audio data
# This will represent our "frame structure" concept in a rudimentary way
frequency = 440  # Frequency in Hz (A4 note)
duration_ms = 5000  # Duration in milliseconds of the generated tone

# Generate the sine wave tone
tone = Sine(frequency).to_audio_segment(duration=duration_ms)

# Setting up multiple frames (in a very basic representation)
# by concatenating the same tone, simulating multiple frames of data in an MP3 file
frames_to_generate = 5  # Number of frames to simulate
audio_frames = tone
for _ in range(1, frames_to_generate):
    audio_frames += tone

# Export the generated frames as an MP3 file
audio_frames.export("./tmp/generated_frames.mp3", format="mp3")

# Variable Speed Playback Feature
# Speed up the playback by a factor (e.g., 1.5 for 50% faster, 0.5 for 50% slower)
speed_change_factor = 1.5
# Changing speed without changing pitch requires complex signal processing algorithms
# not directly available in pydub, but changing speed along with pitch can be done
# by changing the frame rate. This simulates speed change in a very rudimentary way.
new_frame_rate = int(audio_frames.frame_rate * speed_change_factor)
# Note: This changes both pitch and speed, real variable speed playback algorithms are more complex
# Set new frame rate
audio_frames_with_speed_change = audio_frames._spawn(audio_frames.raw_data, overrides={
    "frame_rate": new_frame_rate
}).set_frame_rate(audio_frames.frame_rate)

# Export the speed-changed frames as an MP3 file
audio_frames_with_speed_change.export("./tmp/generated_frames_with_speed_change.mp3", format="mp3")