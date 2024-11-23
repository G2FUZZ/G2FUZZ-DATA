import os

def create_flv_with_interframe_compression(output_path):
    # FLV file header for a video file with no audio
    flv_header = bytearray([
        0x46, 0x4C, 0x56,  # Signature "FLV"
        0x01,  # Version 1
        0x01,  # Video tags only, no audio
        0x00, 0x00, 0x00, 0x09  # Header length, 9 bytes
    ])

    # FLV body - extended to include Interframe Compression
    flv_body = bytearray([
        0x00, 0x00, 0x00, 0x01,  # Previous tag size 0 (first tag in file)
        0x09,  # Tag type 9 = video
        0x00, 0x00, 0x2A,  # Updated data size to include Interframe example (42 bytes, example)
        0x00, 0x00, 0x00, 0x00,  # Timestamp (0 ms)
        0x00, 0x00, 0x00,  # StreamID always 0
        # Video data (including AVC sequence header and simplistically encoded interframe data)
        0x17, 0x01, 0x00, 0x00, 0x00,  # AVC sequence header
        0x00, 0x00, 0x00, 0x01,  # AVC NALU start
        0x67, 0x64, 0x00, 0x1A,  # SPS (simplified)
        0x00, 0x00, 0x00, 0x01,  # AVC NALU start
        0x68, 0xEE, 0x3C, 0x80,  # PPS (simplified)
        # Interframe (P-frame) example to demonstrate interframe compression
        0x00, 0x00, 0x00, 0x01,  # AVC NALU start (new interframe start)
        0x27,  # NALU type (indicating interframe)
        0x45, 0x00, 0x0F, 0xA0,  # Example interframe data (differences from the previous frame)
    ])

    # Write the header and body to the file
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    with open(os.path.join(output_path, "example_with_interframe.flv"), "wb") as flv_file:
        flv_file.write(flv_header)
        flv_file.write(flv_body)

# Use the function to create an FLV file with "Interframe Compression"
create_flv_with_interframe_compression('./tmp/')