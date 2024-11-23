import os
import struct

def create_flv_header(has_audio=True, has_video=True):
    """Creates the FLV file header."""
    type_flags = (has_audio << 2) | has_video
    flv_header = struct.pack('3sBBI', b'FLV', 0x01, type_flags, 0x09)
    # FLV header is followed by the PreviousTagSize0 which is always 0
    return flv_header + b'\x00\x00\x00\x00'

def create_metadata_tag(width=640, height=480, duration=0, framerate=30):
    """Creates an onMetaData tag with basic video properties."""
    # This is a simplified example. Real metadata would be complex and involve AMF0/AMF3 encoding.
    metadata = f"width={width}\nheight={height}\nduration={duration}\nframerate={framerate}\n".encode()
    data_size = len(metadata)
    timestamp = 0
    stream_id = 0
    # TagType for script data is 18
    return struct.pack('>BIII', 18, data_size, timestamp, stream_id) + metadata

def create_video_tag(data, timestamp=0, frame_type='keyframe'):
    """Creates a video tag. Frame type should be 'keyframe' or 'interframe'."""
    frame_types = {'keyframe': 0x10, 'interframe': 0x20}
    codec_id = 0x07  # AVC (H.264)
    avc_packet_type = 0x01  # 0: AVC sequence header; 1: AVC NALU; 2: AVC end of sequence
    composition_time = 0  # No composition time offset
    # Assuming data is already an AVC NALU without start code
    video_data = struct.pack('>BHB', frame_types[frame_type] | codec_id, avc_packet_type, composition_time) + data
    data_size = len(video_data)
    stream_id = 0
    # TagType for video is 9
    return struct.pack('>BIII', 9, data_size, timestamp, stream_id) + video_data

def create_previous_tag_size(tag):
    """Creates the PreviousTagSize field based on the last tag's size."""
    return struct.pack('>I', len(tag))

# Ensure the output directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Path to the output FLV file
output_path = os.path.join(output_dir, "complex_example.flv")

# FLV file content
flv_content = bytearray(create_flv_header())

# Add metadata tag
metadata_tag = create_metadata_tag()
flv_content.extend(metadata_tag)
flv_content.extend(create_previous_tag_size(metadata_tag))

# Simulate adding a simple keyframe (just an example, not actual video data)
keyframe_data = b'\x00\x00\x01'  # Pretend this is the start of an H.264 keyframe
video_tag = create_video_tag(keyframe_data, 0, 'keyframe')
flv_content.extend(video_tag)
flv_content.extend(create_previous_tag_size(video_tag))

# Write the FLV content to a file
with open(output_path, 'wb') as f:
    f.write(flv_content)

print(f"Generated FLV file at: {output_path}")