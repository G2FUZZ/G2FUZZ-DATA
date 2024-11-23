import os

# Create a directory to store the generated FLV files
os.makedirs('./tmp/', exist_ok=True)

# Generate FLV file with more complex file structures
filename = './tmp/extended_complex_flv_file.flv'
with open(filename, 'wb') as f:
    # FLV header
    f.write(b'FLV\x01\x05\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00\x00')

    # Audio Tags (AAC codec) with different properties
    audio_tag_1 = b'\x08\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00'
    audio_tag_2 = b'\x08\x00\x00\x00\x02\x00\x00\x00\x05\x00\x00\x00\x00'
    audio_tag_3 = b'\x08\x00\x00\x00\x02\x00\x00\x00\x0A\x00\x00\x00\x00'

    # Video Tags (H.264 codec) with different properties
    video_tag_1 = b'\x09\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x00'
    video_tag_2 = b'\x09\x00\x00\x00\x05\x00\x00\x00\x01\x00\x00\x00\x00'
    video_tag_3 = b'\x09\x00\x00\x00\x0A\x00\x00\x00\x00\x00\x00\x00\x00'

    # Script Data with extended metadata information
    script_data = b'\x12\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00\x00'

    # Cue Points for seeking within the FLV file
    cue_point_1 = b'\x08\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00'
    cue_point_2 = b'\x08\x00\x00\x00\x0B\x00\x00\x00\x05\x00\x00\x00\x00'

    f.write(audio_tag_1)
    f.write(video_tag_1)
    f.write(script_data)
    f.write(cue_point_1)

    f.write(audio_tag_2)
    f.write(video_tag_2)
    f.write(script_data)
    f.write(cue_point_2)

    f.write(audio_tag_3)
    f.write(video_tag_3)
    f.write(script_data)

print(f'Extended complex FLV file with additional audio and video tags, script data, metadata, and cue points generated: {filename}')