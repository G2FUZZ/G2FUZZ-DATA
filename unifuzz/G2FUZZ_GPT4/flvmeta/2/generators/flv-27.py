import os
import struct

def create_complex_flv(output_path):
    # FLV file header
    flv_header = bytearray([
        0x46, 0x4C, 0x56,  # "FLV"
        0x01,  # Version 1
        0x01,  # Video tags only
        0x00, 0x00, 0x00, 0x09,  # Header length
    ])

    # Metadata Tag (onMetaData) - Simplified example
    onMetaData = bytearray([
        0x02,  # String type SCRIPTDATASTRING
        0x00, 0x0A,  # String length 10
        0x6F, 0x6E, 0x4D, 0x65, 0x74, 0x61, 0x44, 0x61, 0x74, 0x61,  # "onMetaData"
        0x08,  # ECMA array SCRIPTDATAECMAARRAY
        0x00, 0x00, 0x00, 0x00,  # Array length 0 (for simplicity)
        0x00, 0x00, 0x09  # SCRIPTDATAOBJECTEND
    ])
    metadata_tag = bytearray([
        0x12,  # Tag type SCRIPTDATA
        0x00, 0x00, len(onMetaData),  # Data size
        0x00, 0x00, 0x00, 0x00,  # Timestamp
        0x00, 0x00, 0x00,  # StreamID always 0
    ]) + onMetaData

    # Update metadata tag size to include the 11 bytes of the tag header
    metadata_tag_size = len(metadata_tag) - 11
    metadata_tag[1:4] = struct.pack('>I', metadata_tag_size)[1:]

    # Video Data - Keyframes and Interframes
    video_tags = bytearray()

    # Keyframe (I-frame)
    keyframe_data = bytearray([
        0x17,  # Frame type (1 = keyframe) and CodecID (7 = AVC)
        0x01, 0x00, 0x00, 0x00,  # AVC NALU
        # Example AVC keyframe data (simplified for example purposes)
        0x00, 0x00, 0x00, 0x01, 0x65, 0x88
    ])
    keyframe_tag = bytearray([
        0x09,  # Tag type 9 = video
        0x00, 0x00, len(keyframe_data),  # Data size
        0x00, 0x00, 0x00, 0x00,  # Timestamp (for simplicity, using 0)
        0x00, 0x00, 0x00,  # StreamID always 0
    ]) + keyframe_data
    
    # Update keyframe tag size to include the 11 bytes of the tag header
    keyframe_tag_size = len(keyframe_tag) - 11
    keyframe_tag[1:4] = struct.pack('>I', keyframe_tag_size)[1:]

    video_tags += keyframe_tag

    # Interframe (P-frame)
    interframe_data = bytearray([
        0x27,  # Frame type (2 = interframe) and CodecID (7 = AVC)
        0x01, 0x00, 0x00, 0x00,  # AVC NALU
        # Example AVC interframe data (simplified for example purposes)
        0x00, 0x00, 0x00, 0x01, 0x41, 0x99
    ])
    interframe_tag = bytearray([
        0x09,  # Tag type 9 = video
        0x00, 0x00, len(interframe_data),  # Data size
        0x00, 0x00, 0x1E, 0x84,  # Timestamp (100 ms for example)
        0x00, 0x00, 0x00,  # StreamID always 0
    ]) + interframe_data

    # Update interframe tag size to include the 11 bytes of the tag header
    interframe_tag_size = len(interframe_tag) - 11
    interframe_tag[1:4] = struct.pack('>I', interframe_tag_size)[1:]

    video_tags += interframe_tag

    # Final FLV file assembly
    flv_content = flv_header + metadata_tag + struct.pack('>I', len(metadata_tag)) + video_tags + struct.pack('>I', len(interframe_tag))

    # Write to file
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    with open(os.path.join(output_path, "complex_example.flv"), "wb") as flv_file:
        flv_file.write(flv_content)

# Use the function to create a complex FLV file
create_complex_flv('./tmp/')