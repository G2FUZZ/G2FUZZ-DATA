import struct

def write_flv_file(file_path, metadata):
    with open(file_path, 'wb') as file:
        # FLV header
        file.write(b'FLV\x01\x05\x00\x00\x00\x09\x00\x00\x00\x00')
        
        # PreviousTagSize0 (always 0 for the first tag)
        file.write(b'\x00\x00\x00\x00')
        
        # FLV tag for metadata
        tag_data = create_metadata_tag(metadata)
        file.write(tag_data)
        
def create_metadata_tag(metadata):
    tag_type = 18  # Metadata tag type
    data = create_amf_metadata(metadata)
    tag_size = len(data)
    
    tag_header = struct.pack('>BBB', tag_type, tag_size >> 16 & 0xFF, tag_size >> 8 & 0xFF)
    tag_data = tag_header + struct.pack('>B', tag_size & 0xFF) + data
    
    return tag_data

def create_amf_metadata(metadata):
    amf_data = b'\x02onMetaData'
    amf_data += serialize_amf_data(metadata)
    
    return amf_data

def serialize_amf_data(data):
    amf_data = b''
    
    for key, value in data.items():
        amf_data += serialize_amf_string(key)
        amf_data += serialize_amf_value(value)
    
    return amf_data

def serialize_amf_string(string):
    data = string.encode('utf-8')
    length = len(data)
    return struct.pack('>H', length) + data

def serialize_amf_value(value):
    if isinstance(value, int):
        return b'\x00' + struct.pack('>Q', value)
    elif isinstance(value, float):
        return b'\x01' + struct.pack('>d', value)
    elif isinstance(value, str):
        return b'\x02' + serialize_amf_string(value)
    else:
        raise ValueError(f"Unsupported data type: {type(value)}")

# Metadata for the FLV file
metadata = {
    'duration': 120.5,
    'frame_rate': 30,
    'width': 1920,
    'height': 1080
}

# Generate and save FLV file with metadata
file_path = './tmp/example.flv'
write_flv_file(file_path, metadata)