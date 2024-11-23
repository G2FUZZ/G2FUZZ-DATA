import os
import struct
import datetime

def amf0_string(data):
    """Serialize a string to AMF0 format."""
    return struct.pack('>H', len(data)) + data.encode('utf-8')

def amf0_double(number):
    """Serialize a double (floating point) number to AMF0 format."""
    return b'\x00' + struct.pack('>d', number)

def amf0_boolean(value):
    """Serialize a boolean to AMF0 format."""
    return b'\x01' + (b'\x01' if value else b'\x00')

def amf0_object(obj):
    """Serialize an object (dictionary) to AMF0 format."""
    serialized = b'\x03'  # AMF0 object marker
    for key, value in obj.items():
        serialized += amf0_string(key)
        if isinstance(value, str):
            serialized += b'\x02' + amf0_string(value)
        elif isinstance(value, (int, float)):
            serialized += amf0_double(value)
        elif isinstance(value, bool):
            serialized += amf0_boolean(value)
        elif isinstance(value, dict):
            serialized += amf0_object(value)  # Note: This does not handle nested objects correctly
    serialized += b'\x00\x00\x09'  # AMF0 object end marker
    return serialized

def create_video_tag(timestamp, data):
    """Creates a video tag."""
    # Video tag: FrameType (4 bits) + CodecID (4 bits), AVC packet type, CompositionTime
    # Simulated data for simplicity
    tag_type = b'\x09'  # Video tag
    body = data
    data_size = len(body)
    timestamp_extended = timestamp >> 24
    timestamp &= 0xFFFFFF
    return (tag_type + struct.pack('>BBBH', data_size >> 16, data_size >> 8, data_size & 0xFF, timestamp >> 8) + 
            struct.pack('>B', timestamp & 0xFF) + struct.pack('>B', timestamp_extended) + b'\x00\x00\x00' + body)

def create_audio_tag(timestamp, data):
    """Creates an audio tag."""
    # Audio tag: SoundFormat (4 bits) + SoundRate (2 bits) + SoundSize (1 bit) + SoundType (1 bit)
    # Simulated data for simplicity
    tag_type = b'\x08'  # Audio tag
    body = data
    data_size = len(body)
    timestamp_extended = timestamp >> 24
    timestamp &= 0xFFFFFF
    return (tag_type + struct.pack('>BBBH', data_size >> 16, data_size >> 8, data_size & 0xFF, timestamp >> 8) + 
            struct.pack('>B', timestamp & 0xFF) + struct.pack('>B', timestamp_extended) + b'\x00\x00\x00' + body)

def create_flv_with_complex_features(output_path):
    # FLV header
    flv_header = b'FLV\x01\x05\x00\x00\x00\x09'  # FLV Version 1, Video + Audio, Header Length 9
    # PreviousTagSize0
    previous_tag_size_0 = b'\x00\x00\x00\x00'
    
    # Script tag - onMetaData
    script_tag_start = b'\x12\x00\x00\x00\x00\x00\x00\x00\x00'  # TagType 18 for script data, StreamID 0
    on_meta_data = {
        'onMetaData': {
            'duration': 120,
            'width': 1920,
            'height': 1080,
            'videodatarate': 5000,
            'framerate': 30,
            'videocodecid': 7,  # AVC
            'audiodatarate': 320,
            'audiosamplerate': 44100,
            'audiosamplesize': 16,
            'stereo': True,
            'audiocodecid': 10,  # AAC
            'filesize': 0,  # This will be incorrect as we're not updating it after writing the file
            'creationdate': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'customdata': 'Example of custom metadata',
        },
    }
    
    on_meta_data_serialized = amf0_string('onMetaData') + amf0_object(on_meta_data['onMetaData'])
    
    script_data_length = len(on_meta_data_serialized)
    script_tag_full_length = script_tag_start + struct.pack('>L', script_data_length)[:-1] + on_meta_data_serialized
    script_tag_end = struct.pack('>L', len(script_tag_full_length) + 1)
    
    # Simulated video and audio tags
    video_tag = create_video_tag(1000, b'\x00' * 100)  # Simulated video data
    audio_tag = create_audio_tag(500, b'\x01' * 40)  # Simulated audio data
    
    video_tag_end = struct.pack('>L', len(video_tag) + 1)
    audio_tag_end = struct.pack('>L', len(audio_tag) + 1)
    
    # Write the FLV file
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    with open(os.path.join(output_path, 'complex_video.flv'), 'wb') as f:
        f.write(flv_header)
        f.write(previous_tag_size_0)
        f.write(script_tag_full_length)
        f.write(script_tag_end)
        f.write(video_tag)
        f.write(video_tag_end)
        f.write(audio_tag)
        f.write(audio_tag_end)  # Corrected line
    
    print('FLV file with complex features created.')

# Specify the output directory
output_dir = './tmp/'
create_flv_with_complex_features(output_dir)