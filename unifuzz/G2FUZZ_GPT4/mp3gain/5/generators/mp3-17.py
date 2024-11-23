import os
from pydub import AudioSegment
from pydub.generators import Sine

# Ensure the './tmp/' directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate sine wave audio segments for multi-channel (5.1 surround as an example)
frequency = 440  # A4 note, in Hertz
duration_in_ms = 5000  # Duration in milliseconds
volume = -20.0  # Volume in dB

# Generating different tones for channels to simulate a surround effect
# Front Left and Right, Center, Rear Left and Right, and Subwoofer (LFE)
tones = {
    "FL": Sine(frequency).to_audio_segment(duration=duration_in_ms, volume=volume),
    "FR": Sine(frequency + 50).to_audio_segment(duration=duration_in_ms, volume=volume),
    "C": Sine(frequency + 100).to_audio_segment(duration=duration_in_ms, volume=volume),
    "RL": Sine(frequency + 150).to_audio_segment(duration=duration_in_ms, volume=volume),
    "RR": Sine(frequency + 200).to_audio_segment(duration=duration_in_ms, volume=volume),
    "LFE": Sine(frequency + 250).to_audio_segment(duration=duration_in_ms, volume=volume)
}

# Since PyDub doesn't directly support multi-channel audio,
# we simulate it by merging the channels into a stereo track,
# with each "channel" occupying a specific frequency band.
# A real multi-channel setup would require a more sophisticated library or tool.

# Simple example of merging into a stereo track for demonstration
# This is NOT true multi-channel support, but a workaround for demonstration
stereo_sound = AudioSegment.from_mono_audiosegments(tones["FL"] + tones["C"] + tones["RL"], 
                                                    tones["FR"] + tones["C"] + tones["RR"])

file_path = './tmp/generated_audio_surround.mp3'
# Export the generated audio with a constant bitrate
# Note: MP3 with true multi-channel would need proper encoding beyond PyDub's capabilities
stereo_sound.export(file_path, format="mp3", bitrate="192k")

print(f"Generated mp3 file with simulated multi-channel audio at {file_path}")