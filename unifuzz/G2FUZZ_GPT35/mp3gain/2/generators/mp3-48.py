import os

# Create a directory if it does not exist
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample mp3 file with multiple audio tracks, ID3 tags, and variable bitrates
file_path = './tmp/sample_complex_mp3.mp3'

# Sample audio data for each track
audio_track1 = b"Audio Track 1 data"
audio_track2 = b"Audio Track 2 data"
audio_track3 = b"Audio Track 3 data"

# ID3 tags for each track
id3_tag_track1 = b"ID3 tag for Track 1"
id3_tag_track2 = b"ID3 tag for Track 2"
id3_tag_track3 = b"ID3 tag for Track 3"

# Simulating different bitrates for each track
bitrate_track1 = 128
bitrate_track2 = 192
bitrate_track3 = 256

# Generating the mp3 file with multiple tracks, ID3 tags, and bitrates
mp3_data = audio_track1 + id3_tag_track1 + bitrate_track1.to_bytes(2, byteorder='big') + \
           audio_track2 + id3_tag_track2 + bitrate_track2.to_bytes(2, byteorder='big') + \
           audio_track3 + id3_tag_track3 + bitrate_track3.to_bytes(2, byteorder='big')

with open(file_path, 'wb') as f:
    f.write(mp3_data)

print(f"MP3 file with multiple audio tracks, ID3 tags, and variable bitrates generated at: {file_path}")