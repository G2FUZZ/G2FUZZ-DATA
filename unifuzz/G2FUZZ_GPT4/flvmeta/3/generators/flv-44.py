import os
import struct

def create_flv_header():
    return bytes([
        0x46, 0x4C, 0x56,  # Signature "FLV"
        0x01,  # Version 1
        0x05,  # TypeFlags (audio + video)
        0x00, 0x00, 0x00, 0x09,  # DataOffset, FLV header length
        # FLV Body start
        0x00, 0x00, 0x00, 0x00  # PreviousTagSize0
    ])

def create_onMetaData_tag(width, height, duration, framerate):
    # Simulate onMetaData event with basic video properties
    # This is a very simplified version and does not represent actual AMF encoding
    metadata = f"onMetaData width={width} height={height} duration={duration} framerate={framerate}".encode()
    tag_type = 0x12  # Script data
    data_size = len(metadata)
    timestamp = 0
    stream_id = 0
    return struct.pack('>BIII', tag_type, data_size, timestamp, stream_id) + metadata

def create_video_frame_tag(frame_data, timestamp):
    tag_type = 0x09  # Video tag
    data_size = len(frame_data)
    stream_id = 0
    return struct.pack('>BIII', tag_type, data_size, timestamp, stream_id) + frame_data

def create_audio_frame_tag(frame_data, timestamp):
    tag_type = 0x08  # Audio tag
    data_size = len(frame_data)
    stream_id = 0
    return struct.pack('>BIII', tag_type, data_size, timestamp, stream_id) + frame_data

def write_flv_file(output_path, video_width, video_height, duration, framerate):
    # Ensure the output directory exists
    output_dir = os.path.dirname(output_path)
    os.makedirs(output_dir, exist_ok=True)

    # Create the FLV file content
    flv_content = create_flv_header()
    flv_content += create_onMetaData_tag(video_width, video_height, duration, framerate)

    # Simulate video and audio frames (for demonstration purposes)
    for timestamp in range(0, duration * 1000, int(1000 / framerate)):
        # Simulated video frame
        video_frame_data = b'\x00\x00\x00\x00'  # Placeholder for actual video frame data
        flv_content += create_video_frame_tag(video_frame_data, timestamp)

        # Simulated audio frame
        audio_frame_data = b'\x00\x00'  # Placeholder for actual audio frame data
        flv_content += create_audio_frame_tag(audio_frame_data, timestamp)

        # Update the PreviousTagSize for each tag (not implemented in this snippet)

    # Write the FLV content to the file
    with open(output_path, 'wb') as f:
        f.write(flv_content)

    print(f"Generated FLV file with custom metadata and simulated frames at: {output_path}")

# Example usage
output_path = "./tmp/complex_example.flv"
video_width = 640
video_height = 360
duration = 10  # seconds
framerate = 30  # frames per second
write_flv_file(output_path, video_width, video_height, duration, framerate)