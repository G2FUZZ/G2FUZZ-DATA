import os
from pydub import AudioSegment
from pydub.generators import Sine

# Create the ./tmp/ directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Define the parameters for our silence and sine wave
duration_ms = 3000  # 3 seconds
frequency_hz = 440  # A4 note

# Generate a sine wave sound
sound_mono = Sine(frequency_hz).to_audio_segment(duration=duration_ms)

# Create stereo sound in different modes
# Note: pydub doesn't support direct manipulation of stereo modes like joint stereo.
# As a workaround, we'll demonstrate creating dual channel and mono files (stereo is default for two channels).
# Users should use specialized MP3 encoding software or libraries for advanced stereo mode features.

# Stereo (simply combining two mono sounds into left and right channels)
sound_stereo = sound_mono.overlay(sound_mono, position=0)

# Dual Channel (similar to stereo for demonstration, but conceptually would be two independent mono channels in real applications)
sound_dual_channel = sound_stereo

# Mono (simply the mono sound we generated)
sound_mono = sound_mono.set_channels(1)

# Saving files
sound_stereo.export("./tmp/sound_stereo.mp3", format="mp3", bitrate="192k")
sound_dual_channel.export("./tmp/sound_dual_channel.mp3", format="mp3", bitrate="192k")
sound_mono.export("./tmp/sound_mono.mp3", format="mp3", bitrate="192k")

# Note: This example doesn't implement joint stereo encoding, as it requires more complex MP3 encoding capabilities
# than provided by pydub. Advanced MP3 features such as joint stereo would need a more specialized audio processing library
# or tool that supports low-level MP3 encoding options.