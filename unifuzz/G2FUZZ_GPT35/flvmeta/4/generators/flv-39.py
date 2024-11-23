import os
import struct
import time

def generate_flv_file_with_complex_features():
    # Create a directory if it doesn't exist
    os.makedirs('./tmp/', exist_ok=True)
    
    # Generate FLV file with multiple audio and video tags, script data tags, and timestamp manipulation
    with open('./tmp/complex_features.flv', 'wb') as f:
        # FLV header
        f.write(b'FLV\x01\x05\x00\x00\x00\x09\x00\x00\x00\x00')
        
        # Audio and Video tags
        for i in range(5):
            timestamp = int(time.time()) + i
            # Audio tag
            audio_tag = b'\x08\x00\x00\x00\x05' + struct.pack('>I', timestamp) + b'\x00\x00\x00\x00'
            f.write(audio_tag)
            # Video tag
            video_tag = b'\x09\x00\x00\x00\x05' + struct.pack('>I', timestamp) + b'\x00\x00\x00\x00'
            f.write(video_tag)
        
        # Script data tag
        script_data_tag = b'\x12\x00\x00\x00\x0A\x00\x00\x00\x00\x02\x66\x31\x00\x00\x00\x00\x00'
        f.write(script_data_tag)
        
        print("FLV file with complex features generated successfully.")
        
generate_flv_file_with_complex_features()