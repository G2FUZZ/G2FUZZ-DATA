import numpy as np
from pydub import AudioSegment
from pydub.generators import Sine
import os

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate a 1-second sine wave at 440 Hz
tone = Sine(440).to_audio_segment(duration=1000)

# Save the generated sine wave to a file
file_path = './tmp/original_tone.mp3'
tone.export(file_path, format="mp3")

# Load the MP3 file
audio = AudioSegment.from_mp3(file_path)

# Normalize the audio to a standard volume level
normalized_audio = audio.apply_gain(-audio.dBFS)

# Save the normalized audio
normalized_file_path = './tmp/normalized_tone.mp3'
normalized_audio.export(normalized_file_path, format="mp3")

# Introducing Encoding and Decoding Algorithms feature with custom manipulation
# Simulate an additional "feature" by creating a slight variation in the audio.
# Let's add a fade-in effect to simulate our "additional encoding process"
enhanced_audio = normalized_audio.fade_in(2000)  # 2-second fade-in

# Save the enhanced audio with our "additional feature"
enhanced_file_path = './tmp/enhanced_tone.mp3'
enhanced_audio.export(enhanced_file_path, format="mp3")

# Encoding Presets and Modes
voice_preset_audio = enhanced_audio.set_frame_rate(16000)  # Lower sample rate for voice
voice_preset_audio = voice_preset_audio.set_channels(1)  # Mono channel for voice

# Save the audio with our simulated "voice preset"
voice_preset_file_path = './tmp/voice_preset_tone.mp3'
voice_preset_audio.export(voice_preset_file_path, format="mp3", bitrate="32k")

# Simulate the Bit Reservoir feature
bit_reservoir_file_path = './tmp/bit_reservoir_tone.mp3'
voice_preset_audio.export(bit_reservoir_file_path, format="mp3", parameters=["-q:a", "0", "-vbr", "2"])

# Backward Compatibility feature
# Since MP3 is inherently backward compatible, we simulate this by ensuring the MP3
# is encoded with settings compatible with both new and old decoders.
# This step is more about ensuring the file can be played on older devices,
# so we'll use a common setting that should ensure broad compatibility.
backward_compatible_audio = voice_preset_audio

# Save the audio with our simulated "Backward Compatibility" feature
backward_compatible_file_path = './tmp/backward_compatible_tone.mp3'
backward_compatible_audio.export(backward_compatible_file_path, format="mp3", bitrate="128k")

print(f"Original, normalized, enhanced, voice preset, and Bit Reservoir, Backward Compatibility MP3 files saved to './tmp/'")