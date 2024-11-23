import os
from pydub import AudioSegment
from pydub.generators import Sine

# Ensure the './tmp/' and subdirectories for each channel exist
base_dir = './tmp/surround'
channel_dirs = ['FL', 'FR', 'C', 'RL', 'RR', 'LFE']
for channel in channel_dirs:
    os.makedirs(os.path.join(base_dir, channel), exist_ok=True)

# Generate sine wave audio segments for multi-channel (5.1 surround as an example)
frequency = 440  # A4 note, in Hertz
duration_in_ms = 5000  # Duration in milliseconds
volume = -20.0  # Volume in dB

# Generating different tones for channels to simulate a surround effect
tones = {
    "FL": Sine(frequency).to_audio_segment(duration=duration_in_ms, volume=volume),
    "FR": Sine(frequency + 50).to_audio_segment(duration=duration_in_ms, volume=volume),
    "C": Sine(frequency + 100).to_audio_segment(duration=duration_in_ms, volume=volume),
    "RL": Sine(frequency + 150).to_audio_segment(duration=duration_in_ms, volume=volume),
    "RR": Sine(frequency + 200).to_audio_segment(duration=duration_in_ms, volume=volume),
    "LFE": Sine(frequency + 250).to_audio_segment(duration=duration_in_ms, volume=volume)
}

# Export the generated audio for each channel into its own file within its respective directory
for channel, tone in tones.items():
    file_path = os.path.join(base_dir, channel, f'generated_audio_{channel}.mp3')
    tone.export(file_path, format="mp3", bitrate="192k")
    print(f"Generated mp3 file for {channel} channel at {file_path}")

# Note:
# This setup creates six separate MP3 files, one for each channel of a 5.1 surround setup.
# Playback or synthesis of true surround sound from these files would require additional steps
# not covered by this script, such as using a multi-channel audio playback system or software 
# that can properly interpret and play back the separate channel files in sync.