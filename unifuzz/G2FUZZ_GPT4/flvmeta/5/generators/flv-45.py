import os
import struct
from datetime import datetime

def create_complex_flv_file():
    # Ensure the tmp directory exists
    if not os.path.exists('./tmp'):
        os.makedirs('./tmp')

    # Path to the FLV file to be created
    flv_file_path = './tmp/complex_video_stream.flv'

    # FLV file header for a video file without audio
    flv_header = bytes('FLV\x01\x05\x00\x00\x00\x09', 'latin1')

    # PreviousTagSize0 always follows the FLV header for the first tag, set to 0
    previous_tag_size_0 = (0).to_bytes(4, byteorder='big')

    # Opening the FLV file for binary write
    with open(flv_file_path, 'wb') as flv_file:
        flv_file.write(flv_header)
        flv_file.write(previous_tag_size_0)

        # onMetaData tag to include video dimensions and duration
        metadata_object = {
            "duration": 0.0,
            "width": 640.0,
            "height": 360.0,
            "videodatarate": 0.0,
            "framerate": 24.0,
            "videocodecid": 7.0,  # AVC
            "filesize": 0.0
        }
        metadata_body = encode_amf0("onMetaData") + encode_amf0(metadata_object)
        data_tag = construct_data_tag(metadata_body)
        flv_file.write(data_tag)
        flv_file.write(len(data_tag).to_bytes(4, byteorder='big'))

        # Simulate a sequence of video frames (here, just using dummy data for demonstration)
        for i in range(1, 25):  # Simulate 1 second of video at 24 fps
            # Video tag content (Dummy data)
            frame_type = 1  # keyframe
            codec_id = 7  # AVC
            avc_packet_type = 1  # NALU
            composition_time = 0
            video_data = b'\x00\x00\x00\x01'  # Fake NALU start code

            video_tag_body = struct.pack('>BHB', (frame_type << 4) | codec_id, avc_packet_type, composition_time) + video_data
            video_tag = construct_video_tag(video_tag_body)
            flv_file.write(video_tag)

            # Writing the PreviousTagSize for video tag
            flv_file.write(len(video_tag).to_bytes(4, byteorder='big'))

        print(f"Complex FLV file created at {flv_file_path}")

def construct_data_tag(data):
    """Constructs a script data tag."""
    tag_type = 18  # script data
    data_length = len(data)
    timestamp = 0
    stream_id = 0
    # Adjusted struct.pack format to correctly handle the parameters
    return struct.pack('>BIII', tag_type, data_length, timestamp, stream_id) + data

def construct_video_tag(data):
    """Constructs a video tag."""
    tag_type = 9  # video tag
    data_length = len(data)
    timestamp = 0
    stream_id = 0
    # Adjusted struct.pack format to correctly handle the parameters
    return struct.pack('>BIII', tag_type, data_length, timestamp, stream_id) + data

def encode_amf0(data):
    """Encodes data into AMF0 format."""
    if isinstance(data, str):
        return struct.pack('>B', 2) + struct.pack('>H', len(data)) + data.encode('utf-8')
    elif isinstance(data, dict):
        encoded = struct.pack('>B', 3)  # Object type
        for key, value in data.items():
            encoded += struct.pack('>H', len(key)) + key.encode('utf-8')
            encoded += encode_amf0(value)
        encoded += struct.pack('>H', 0) + b'\x09'  # Object end marker
        return encoded
    elif isinstance(data, float):
        return struct.pack('>B', 0) + struct.pack('>d', data)
    else:
        raise TypeError("Unsupported type for AMF0 encoding")

create_complex_flv_file()