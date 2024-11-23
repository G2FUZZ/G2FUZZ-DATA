import os
import numpy as np
from pydub import AudioSegment

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Function to generate a sine wave tone
def generate_tone(frequency=440, duration_ms=1000, volume=0.5, sample_rate=44100):
    t = np.linspace(0, duration_ms / 1000, int(sample_rate * (duration_ms / 1000)), False)
    wave = np.sin(frequency * t * 2 * np.pi)
    # Normalize to 16-bit range
    audio = wave * (2**15 - 1) * volume
    # Ensure data type is int16
    audio = audio.astype(np.int16)
    return audio

# Generate a tone for left and right channels
left_channel = generate_tone(frequency=440, volume=0.5)  # A4 note
right_channel = generate_tone(frequency=660, volume=0.5)  # E5 note, creates a stereo effect

# Create stereo audio segment
stereo_audio = AudioSegment.from_mono_audiosegments(AudioSegment(left_channel.tobytes(), sample_width=2, frame_rate=44100, channels=1),
                                                    AudioSegment(right_channel.tobytes(), sample_width=2, frame_rate=44100, channels=1))

# Save stereo mode (for joint stereo and dual channel, this approach is a simplification)
stereo_audio.export("./tmp/stereo_mode.mp3", format="mp3")

# Create and save a mono file by mixing down the stereo file
mono_audio = stereo_audio.set_channels(1)
mono_audio.export("./tmp/mono_mode.mp3", format="mp3")

# Joint Stereo Mode Enhancements
# Note: The pydub library does not directly support setting joint stereo mode enhancements.
# However, we can simulate a joint stereo effect by manually adjusting the channels before exporting.
# This code does not provide a direct way to apply real joint stereo encoding as it's a feature of the MP3 encoding process,
# typically handled by the encoder based on the encoding settings.
# For demonstration, we'll encode it with a higher bitrate which generally includes better handling for stereo effects,
# but keep in mind this does not explicitly set the joint stereo mode.
joint_stereo_audio = AudioSegment.from_mono_audiosegments(AudioSegment(left_channel.tobytes(), sample_width=2, frame_rate=44100, channels=1),
                                                          AudioSegment(right_channel.tobytes(), sample_width=2, frame_rate=44100, channels=1))
joint_stereo_audio.export("./tmp/joint_stereo_mode.mp3", format="mp3", bitrate="192k")

print("MP3 files generated in './tmp/' directory.")