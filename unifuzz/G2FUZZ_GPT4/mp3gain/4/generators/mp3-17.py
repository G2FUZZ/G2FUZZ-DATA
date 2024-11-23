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
# PyDub doesn’t directly expose encoding presets and modes via its API.
# However, we can simulate changing encoding presets by manipulating the parameters
# in the export method, such as "bitrate", "parameters" (which can include command-line
# options for the underlying ffmpeg process), or changing the format.
# For demonstration, let's simulate using a "voice" preset by lowering the bitrate,
# which is commonly done for voice to save space while maintaining intelligibility.

# This step is conceptual and intended to simulate the idea of using a "voice" preset.
voice_preset_audio = enhanced_audio.set_frame_rate(16000)  # Lower sample rate for voice
voice_preset_audio = voice_preset_audio.set_channels(1)  # Mono channel for voice

# Save the audio with our simulated "voice preset"
voice_preset_file_path = './tmp/voice_preset_tone.mp3'
voice_preset_audio.export(voice_preset_file_path, format="mp3", bitrate="32k")

print(f"Original, normalized, enhanced, and voice preset MP3 files saved to './tmp/'")