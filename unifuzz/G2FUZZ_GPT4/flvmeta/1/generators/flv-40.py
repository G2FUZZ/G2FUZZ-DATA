import os
import random

def create_flv_with_drm_and_frames(output_path, num_frames=5):
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # FLV header for a video file with no audio
    # FLV version 1, has video, no audio, header length 9
    flv_header = bytearray([0x46, 0x4C, 0x56, 0x01, 0x01, 0x00, 0x00, 0x00, 0x09])
    
    # PreviousTagSize0 always 0 for the first tag after the FLV header
    previous_tag_size = bytearray([0x00, 0x00, 0x00, 0x00])
    
    # Construct a script data object (onMetaData) with DRM info and more
    script_data_tag = bytearray([
        0x12,  # Tag type script data
        0x00, 0x00, 0x00,  # Data size to be adjusted later
        0x00, 0x00, 0x00, 0x00,  # Timestamp (0 for metadata)
        0x00, 0x00, 0x00,  # StreamID always 0
        0x02, 0x00, 0x0A,  # String marker and length
        0x6F, 0x6E, 0x4D, 0x65, 0x74, 0x61, 0x44, 0x61, 0x74, 0x61,  # 'onMetaData' string
        0x08, 0x00, 0x00, 0x00, 0x03,  # ECMA array marker and length (3 for DRM, width, height)
        # DRM key-value
        0x00, 0x03,  # DRM key length
        0x44, 0x52, 0x4D,  # 'DRM'
        0x02, 0x00, 0x0F,  # Type String, length of the value
        0x45, 0x6E, 0x61, 0x62, 0x6C, 0x65, 0x64, 0x20, 0x77, 0x69, 0x74, 0x68, 0x20, 0x44, 0x52, 0x4D,  # 'Enabled with DRM'
        # Width key-value
        0x00, 0x05,  # Width key length
        0x57, 0x69, 0x64, 0x74, 0x68,  # 'Width'
        0x00,  # Type Number
        0x40, 0x90, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,  # 640.0
        # Height key-value
        0x00, 0x06,  # Height key length
        0x48, 0x65, 0x69, 0x67, 0x68, 0x74,  # 'Height'
        0x00,  # Type Number
        0x40, 0x8E, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,  # 360.0
    ])
    
    # Adjust the script data size
    script_data_size = len(script_data_tag) - 11  # Subtract the tag header size
    script_data_tag[1:4] = (script_data_size >> 16) & 0xFF, (script_data_size >> 8) & 0xFF, script_data_size & 0xFF
    
    # Calculate the script data tag size and append it as PreviousTagSize at the end of the tag
    script_tag_size = bytearray([
        (script_data_size >> 24) & 0xFF,
        (script_data_size >> 16) & 0xFF,
        (script_data_size >> 8) & 0xFF,
        script_data_size & 0xFF,
    ])
    script_data_tag += script_tag_size
    
    # Dummy video frame data (keyframe, AVC, frame type "1" - key frame, codec ID "7" - AVC)
    video_frame_header = bytearray([0x09, 0x00, 0x00, 0x05, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x17, 0x01, 0x00, 0x00, 0x00])
    video_frame_data = bytearray([0x00, 0x00, 0x00, 0x01, 0x67]) + bytearray(random.getrandbits(8) for _ in range(5))  # SPS
    video_frame_data += bytearray([0x00, 0x00, 0x00, 0x01, 0x68]) + bytearray(random.getrandbits(8) for _ in range(5))  # PPS
    video_frame_size = len(video_frame_data) + 5  # Add header size excluding tag type and data size fields
    video_frame_header[1:4] = (video_frame_size >> 16) & 0xFF, (video_frame_size >> 8) & 0xFF, video_frame_size & 0xFF
    
    # Write the FLV file
    with open(output_path, 'wb') as f:
        f.write(flv_header)
        f.write(previous_tag_size)
        f.write(script_data_tag)
        
        for i in range(num_frames):
            f.write(video_frame_header)
            f.write(video_frame_data)
            # Adjust for the next frame
            video_frame_header[4:7] = bytearray([0x00, 0x00, (i+1) * 40])  # Simple timestamp increment
            
            # PreviousTagSize for video frames
            video_frame_total_size = 11 + len(video_frame_data)
            previous_tag_size[0], previous_tag_size[1], previous_tag_size[2], previous_tag_size[3] = video_frame_total_size >> 24, video_frame_total_size >> 16 & 0xFF, video_frame_total_size >> 8 & 0xFF, video_frame_total_size & 0xFF
            f.write(previous_tag_size)

if __name__ == "__main__":
    create_flv_with_drm_and_frames('./tmp/complex_example_with_drm.flv')