import os
import struct
import random

def create_enhanced_flv_with_drm_and_audio(output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    flv_header = bytearray([0x46, 0x4C, 0x56, 0x01, 0x05, 0x00, 0x00, 0x00, 0x09])
    previous_tag_size_0 = bytearray([0x00, 0x00, 0x00, 0x00])

    on_metadata = construct_script_data({
        "duration": 0.0,
        "width": 1920,
        "height": 1080,
        "videodatarate": 0,
        "framerate": 24.0,
        "videocodecid": 7,  # AVC
        "audiocodecid": 10,  # AAC
        "audiosamplerate": 44100,
        "audiosamplesize": 16,
        "stereo": True,
        "DRM": "Enabled with advanced DRM",
    })

    # Create multiple video frames
    video_frames = [construct_video_frame(timestamp=i*40) for i in range(1, 6)]  # Example: 5 frames
    
    # Create an AAC audio tag
    aac_audio_tag = construct_audio_frame()

    with open(output_path, 'wb') as f:
        f.write(flv_header)
        f.write(previous_tag_size_0)
        f.write(on_metadata)
        
        previous_tag_size = struct.pack('>I', len(on_metadata))
        f.write(previous_tag_size)

        for frame in video_frames:
            f.write(frame)
            previous_tag_size = struct.pack('>I', len(frame))
            f.write(previous_tag_size)
        
        f.write(aac_audio_tag)
        # Further audio/video tags would be appended similarly

def construct_script_data(metadata):
    script_data_tag = bytearray([
        0x12,
        0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00,
    ])
    
    script_data = bytearray([
        0x02, 0x00, 0x0A,
        0x6F, 0x6E, 0x4D, 0x65, 0x74, 0x61, 0x44, 0x61, 0x74, 0x61
    ])
    
    script_data += construct_ecma_array(metadata)
    
    data_size = len(script_data)
    script_data_tag[1:4] = struct.pack('>I', data_size)[1:]
    
    return script_data_tag + script_data

def construct_ecma_array(metadata):
    ecma_array = bytearray([0x08]) + struct.pack('>I', len(metadata))
    
    for key, value in metadata.items():
        key_encoded = key.encode('utf-8')
        ecma_array += struct.pack('>H', len(key_encoded)) + key_encoded
        
        if isinstance(value, str):
            value_encoded = value.encode('utf-8')
            ecma_array += bytearray([0x02]) + struct.pack('>H', len(value_encoded)) + value_encoded
        elif isinstance(value, (int, float)):
            ecma_array += bytearray([0x00]) + struct.pack('>d', float(value))

    ecma_array += bytearray([0x00, 0x00, 0x09])
    return ecma_array

def construct_video_frame(timestamp=0):
    frame_size = 14
    video_data = bytearray([
        0x09,
        0x00, 0x00, 0x0E,
        (timestamp >> 16) & 0xFF, (timestamp >> 8) & 0xFF, timestamp & 0xFF,
        (timestamp >> 24) & 0xFF,
        0x00, 0x00, 0x00,
        0x17, 0x01, 0x00, 0x00, 0x00,
    ])
    return video_data

def construct_audio_frame():
    # Example of a simple AAC audio frame tag
    frame_size = 11  # Placeholder size
    audio_data = bytearray([
        0x08,  # Tag type audio
        0x00, 0x00, 0x0B,  # Data size
        0x00, 0x00, 0x00,  # Timestamp
        0x00,  # TimestampExtended
        0x00, 0x00, 0x00,  # StreamID always 0
        0xAF, 0x01,  # AAC raw frame
        # Actual AAC raw frame data would go here
    ])
    return audio_data

if __name__ == "__main__":
    create_enhanced_flv_with_drm_and_audio('./tmp/enhanced_example_with_drm_and_audio.flv')