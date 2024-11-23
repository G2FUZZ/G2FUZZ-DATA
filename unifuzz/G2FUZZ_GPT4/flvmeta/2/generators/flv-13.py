import os

def create_flv_with_seek_points_and_partial_playback(output_path):
    # FLV file header for a video file with no audio
    # This is a very simplistic approach and not fully compliant with the spec
    flv_header = bytearray([
        0x46, 0x4C, 0x56,  # Signature "FLV"
        0x01,  # Version 1
        0x01,  # Video tags only, no audio
        0x00, 0x00, 0x00, 0x09  # Header length, 9 bytes
    ])

    # FLV body - simplified example to simulate seek points and partial playback
    # In a real FLV file, this section would include a series of tags (video/audio/script)
    # For simplicity, we're just adding a placeholder for video data and simulating partial download
    flv_body = bytearray([
        0x00, 0x00, 0x00, 0x01,  # Previous tag size 0 (first tag in file)
        # Tag type 9 = video
        0x09,
        0x00, 0x00, 0x1A,  # Data size (26 bytes, example)
        0x00, 0x00, 0x00, 0x00,  # Timestamp (0 ms)
        0x00, 0x00, 0x00,  # StreamID always 0
        # Video data (simplistic placeholder)
        0x17, 0x01, 0x00, 0x00, 0x00,  # AVC sequence header
        0x00, 0x00, 0x00, 0x01,  # AVC NALU start
        0x67, 0x64, 0x00, 0x1A,  # SPS (simplified)
        0x00, 0x00, 0x00, 0x01,  # AVC NALU start
        0x68, 0xEE, 0x3C, 0x80,  # PPS (simplified)
        # Simulate partial download by splitting video data into chunks
        # In a real scenario, this would be handled by the server/client during the download process
    ])

    # Note: This example does not create real seek points or a proper index for partial downloads.
    # Implementing functionality for actual partial download and playback would involve server-side support for HTTP range requests and client-side handling.

    # Write the header and body to the file
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    with open(os.path.join(output_path, "example_with_partial_playback.flv"), "wb") as flv_file:
        flv_file.write(flv_header)
        flv_file.write(flv_body)

# Use the function to create an FLV file with "seek points" and partial playback feature
create_flv_with_seek_points_and_partial_playback('./tmp/')