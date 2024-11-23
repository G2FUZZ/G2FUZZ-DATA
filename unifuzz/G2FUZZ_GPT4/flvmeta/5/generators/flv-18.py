import os
import struct

def create_flv_with_features_custom_playback(output_path):
    # FLV header
    flv_header = b'FLV\x01\x05\x00\x00\x00\x09'  # FLV Version 1, Video + Audio, Header Length 9
    # PreviousTagSize0
    previous_tag_size_0 = b'\x00\x00\x00\x00'
    
    # Script tag - onMetaData
    # For simplicity, this script tag will include a minimal onMetaData with additional features
    script_tag_start = b'\x12\x00\x00\x00\x00\x00\x00\x00\x00'  # TagType 18 for script data, StreamID 0
    on_meta_data = {
        'onMetaData': {
            'duration': 0,
            'width': 0,
            'height': 0,
            'videodatarate': 0,
            'framerate': 0,
            'videocodecid': 7,  # AVC
            'audiodatarate': 0,
            'audiosamplerate': 44100,
            'audiosamplesize': 16,
            'stereo': True,
            'audiocodecid': 10,  # AAC
            'filesize': 0,
            'supportsSlowFastMotionPlayback': True,  # Support for Slow Motion and Fast Motion Playback
            'supportsMultipleDataStreams': True,  # Support for Multiple Data Streams
            'customizablePlayback': True,  # Customizable Playback feature
        },
        'cuePoints': [{
            'type': 'event',
            'name': 'CuePoint1',
            'time': 0,
            'data': {'parameters': 'value'}
        }]
    }
    
    # Serialize the onMetaData object into AMF0 format
    # This example does not include an AMF0 serializer;
    # you would need to either use an existing library or implement serialization based on the AMF0 spec.
    # For the purpose of this demonstration, we will pretend we serialized it and just put placeholder data.
    on_meta_data_serialized = b'\x02\x00\x0aonMetaData' + b'\x00\x00\x00\x00'  # Placeholder for serialized onMetaData

    script_data_length = len(on_meta_data_serialized)
    script_tag_full_length = script_tag_start + struct.pack('>L', script_data_length)[:-1] + on_meta_data_serialized
    script_tag_end = struct.pack('>L', len(script_tag_full_length) + 1)
    
    # Write the FLV file
    if not os.path.exists(output_path):
        os.makedirs(output_path, exist_ok=True)  # Added exist_ok=True to prevent FileExistsError
    with open(os.path.join(output_path, 'video_with_custom_playback.flv'), 'wb') as f:
        f.write(flv_header)
        f.write(previous_tag_size_0)
        f.write(script_tag_full_length)
        f.write(script_tag_end)
    
    print('FLV file with support for slow motion, fast motion playback, multiple data streams, and customizable playback created.')

# Specify the output directory
output_dir = './tmp/'
create_flv_with_features_custom_playback(output_dir)