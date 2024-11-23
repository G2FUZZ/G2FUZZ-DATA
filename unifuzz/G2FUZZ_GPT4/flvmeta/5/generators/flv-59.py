import os
import struct

def create_complex_flv_file():
    # Ensure the tmp directory exists
    if not os.path.exists('./tmp'):
        os.makedirs('./tmp')

    # Path to the FLV file to be created
    flv_file_path = './tmp/complex_structure.flv'

    # FLV header for a video file
    flv_header = bytes('FLV\x01\x05\x00\x00\x00\x09', 'latin1')

    # PreviousTagSize0 always follows the FLV header for the first tag, set to 0
    previous_tag_size_0 = (0).to_bytes(4, byteorder='big')

    # onMetaData tag - a script tag that contains various metadata about the FLV file
    # In a real scenario, these values should be calculated based on the actual video data
    metadata = {
        "duration": 120.0,  # Duration in seconds
        "width": 1280,
        "height": 720,
        "videocodecid": 7,  # AVC
        "framerate": 25.0,
        "videodatarate": 1500  # In kilobits per second
    }
    # Serialize metadata into a script data object (AMF0 encoded for onMetaData)
    metadata_serialized = serialize_amf0("onMetaData") + serialize_amf0(metadata)

    data_tag_header = bytes([18])  # Script data tag
    metadata_length = len(metadata_serialized)
    data_tag = data_tag_header + metadata_length.to_bytes(3, byteorder='big') + (0).to_bytes(3, byteorder='big') + (0).to_bytes(4, byteorder='big') + metadata_serialized

    with open(flv_file_path, 'wb') as flv_file:
        flv_file.write(flv_header)
        flv_file.write(previous_tag_size_0)
        flv_file.write(data_tag)
        flv_file.write(len(data_tag).to_bytes(4, byteorder='big'))

        # Adding a fake video tag to simulate video data
        video_data = b'\x00' * 4000  # Placeholder for video frame data
        video_tag_header = bytes([9])  # Video tag
        video_data_length = len(video_data)
        video_tag = video_tag_header + video_data_length.to_bytes(3, byteorder='big') + (0).to_bytes(3, byteorder='big') + (0).to_bytes(4, byteorder='big') + video_data
        flv_file.write(video_tag)
        flv_file.write(len(video_tag).to_bytes(4, byteorder='big'))

    print(f"Complex FLV file created at {flv_file_path}")

def serialize_amf0(data):
    """
    A very simple serializer for AMF0 data. This function only handles strings and dictionaries (objects),
    which is sufficient for a basic onMetaData tag. For full AMF0 support, use a library or extend this function.
    """
    if isinstance(data, str):
        return b'\x02' + struct.pack('>H', len(data)) + data.encode('utf-8')
    elif isinstance(data, dict):
        buf = b'\x03'  # Object start marker
        for key, value in data.items():
            buf += struct.pack('>H', len(key)) + key.encode('utf-8')
            if isinstance(value, (float, int)):  # Simplified: treating all numbers as floats
                buf += b'\x00' + struct.pack('>d', float(value))  # Number type marker and value
            else:
                raise ValueError("Unsupported value type for AMF0 serialization")
        buf += b'\x00\x00\x09'  # Object end marker
        return buf
    else:
        raise ValueError("Unsupported data type for AMF0 serialization")

create_complex_flv_file()