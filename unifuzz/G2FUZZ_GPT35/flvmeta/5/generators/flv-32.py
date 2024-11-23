import os

# Create a directory for storing FLV files
os.makedirs('./tmp/', exist_ok=True)

# Generate FLV file with multiple audio tracks, video tags, script data, and cue points
header = b'FLV\x01\x05\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00\x00'
audio_data_1 = b'\x00\x00\x00\x13\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
audio_data_2 = b'\x00\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
video_data = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
script_data = b'\x00\x00\x00\x04\x00\x00\x00\x15\x00\x00\x00\x00\x00\x00\x00\x00'
cue_points = b'\x00\x00\x00\x05\x00\x00\x00\x16\x00\x00\x00\x00\x00\x00\x00\x00'

with open('./tmp/sample_with_complex_features.flv', 'wb') as f:
    f.write(header)
    f.write(audio_data_1)
    f.write(audio_data_2)
    f.write(video_data)
    f.write(script_data)
    f.write(cue_points)

print('FLV file with complex features generated successfully.')