import os

# Create a directory to store the generated FLV files
os.makedirs('./tmp/', exist_ok=True)

# Generate FLV file with multiple audio and video tags, script data, and metadata
filename = './tmp/complex_flv_file.flv'
with open(filename, 'wb') as f:
    # FLV header
    f.write(b'FLV\x01\x05\x00\x00\x00\x09\x00\x00\x00\x00\x00\x00\x00\x00')

    # Audio Tags (AAC codec) with different sampling rates and bitrates
    audio_tag_1 = b'\x08\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00'
    audio_tag_2 = b'\x08\x00\x00\x00\x02\x00\x00\x00\x05\x00\x00\x00\x00'
    
    # Video Tags (H.264 codec) with different frame sizes and keyframe flags
    video_tag_1 = b'\x09\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x00'
    video_tag_2 = b'\x09\x00\x00\x00\x05\x00\x00\x00\x01\x00\x00\x00\x00'
    
    # Script Data with metadata information
    script_data = b'\x12\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00\x00'
    
    f.write(audio_tag_1)
    f.write(video_tag_1)
    f.write(script_data)
    f.write(audio_tag_2)
    f.write(video_tag_2)

print(f'Complex FLV file with multiple audio and video tags, script data, and metadata generated: {filename}')