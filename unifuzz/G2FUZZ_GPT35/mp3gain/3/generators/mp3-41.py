import os
from pydub import AudioSegment
from pydub.generators import Sine

# Create a stereo mp3 file with ID3 tags, custom metadata, and variable bitrate encoding
stereo_sound_extended = Sine(880).to_audio_segment(duration=2000)
# Add ID3 tags
stereo_sound_extended.export("./tmp/stereo_sound_extended.mp3", format="mp3", tags={'title': 'Extended Stereo Sound', 'artist': 'PyDub'})

# Add custom metadata
custom_metadata = "Custom Metadata: This mp3 file contains additional information embedded within."
stereo_sound_extended += AudioSegment.silent(duration=len(custom_metadata)*1000)

# Add variable bitrate encoding
stereo_sound_extended.export("./tmp/stereo_sound_extended_vbr.mp3", format="mp3", bitrate="256k")

custom_metadata_file_path = "/tmp/custom_metadata.txt"
if os.path.exists(custom_metadata_file_path):
    stereo_sound_extended = stereo_sound_extended.overlay(AudioSegment.from_file(custom_metadata_file_path), position=0)
    stereo_sound_extended.export("./tmp/stereo_sound_extended_with_metadata.mp3", format="mp3")
else:
    print(f"Error: File '{custom_metadata_file_path}' not found.")