import os
import struct
import time

def create_complex_flv_file():
    # Ensure the tmp directory exists
    if not os.path.exists('./tmp'):
        os.makedirs('./tmp')
    
    # Path to the FLV file to be created
    flv_file_path = './tmp/complex_features_demo.flv'
    
    # FLV file header: 'FLV', version 1, flags (video tag present, audio tag present), header size
    flv_header = bytes('FLV\x01\x05\x00\x00\x00\x09', 'latin1')
    
    # PreviousTagSize0 always follows the FLV header for the first tag, set to 0
    previous_tag_size_0 = (0).to_bytes(4, byteorder='big')
    
    # Opening the file to write binary data
    with open(flv_file_path, 'wb') as flv_file:
        flv_file.write(flv_header)
        flv_file.write(previous_tag_size_0)
        
        # Custom metadata with more complex structures
        metadata = {
            "creator": "Advanced FLV Generator",
            "hasVideo": True,
            "hasAudio": True,
            "canSeekToEnd": True,
            "simulatedFrames": 3,
            "features": ["Custom Encoding", "Simulated Frames", "Advanced Playback"]
        }
        
        # Serialize metadata to a string (simple representation for demonstration)
        metadata_str = str(metadata)
        metadata_length = len(metadata_str)
        
        # Script Data tag for custom metadata
        script_data_tag = bytes([18]) + metadata_length.to_bytes(3, byteorder='big') + (0).to_bytes(3, byteorder='big') + (0).to_bytes(4, byteorder='big') + bytes(metadata_str, 'latin1')
        flv_file.write(script_data_tag)
        flv_file.write(len(script_data_tag).to_bytes(4, byteorder='big'))
        
        # Simulate video frames
        for i in range(1, 4):
            # Simulated video data (random content for demonstration)
            frame_data = f"SimulatedFrame{i}".encode('latin1')
            frame_length = len(frame_data)
            
            # Timestamp increment (just for demonstration)
            timestamp = i * 1000  # 1 second apart
            
            # Video tag: Frame type (key frame) + Codec ID (AVC)
            video_tag_type = bytes([0x17])
            # CompositionTime (only for AVC, set to 0)
            composition_time = (0).to_bytes(3, byteorder='big')
            
            # Construct video tag
            video_tag = (video_tag_type +
                         frame_length.to_bytes(3, byteorder='big') +
                         struct.pack('>I', timestamp)[:3] +  # Timestamp, only 3 bytes
                         composition_time +  # Composition time for AVC
                         (0).to_bytes(4, byteorder='big') +  # StreamID, always 0
                         frame_data)
            
            flv_file.write(video_tag)
            flv_file.write(len(video_tag).to_bytes(4, byteorder='big'))
        
        print(f"Complex FLV file created at {flv_file_path}")

create_complex_flv_file()