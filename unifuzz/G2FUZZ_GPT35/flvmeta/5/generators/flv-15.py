import os

# Create a directory for storing FLV files
os.makedirs('./tmp/', exist_ok=True)

# Generate FLV file with header, body, metadata tag, and caption/subtitle support
header = b'FLV\x01\x01\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00\x00'
audio_data = b'\x00\x00\x00\x13\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
video_data = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
metadata_tag = b'\x00\x00\x00\x02\x00\x00\x00\x0a\x00\x00\x00\x00\x00\x00\x00\x00'
captioning_subtitle = b'\x00\x00\x00\x03\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x00\x00\x00'

with open('./tmp/sample_with_subtitle.flv', 'wb') as f:
    f.write(header)
    f.write(audio_data)
    f.write(video_data)
    f.write(metadata_tag)
    f.write(captioning_subtitle)

print('FLV file with Captioning/Subtitle Support generated successfully.')