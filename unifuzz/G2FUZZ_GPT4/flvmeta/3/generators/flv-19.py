import os

# Ensure the tmp directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Path to the output FLV file
output_path = os.path.join(output_dir, "example_with_looping_support.flv")

# FLV file header and metadata for a video tag to simulate embedding capabilities
flv_header = bytes([
    0x46, 0x4C, 0x56,  # Signature "FLV"
    0x01,  # Version 1
    0x05,  # TypeFlags (audio + video)
    0x00, 0x00, 0x00, 0x09,  # DataOffset, FLV header length
    # FLV Body start
    0x00, 0x00, 0x00, 0x00  # PreviousTagSize0
])

# Sample video tag
video_tag = bytes([
    0x12,  # Tag type script
    0x00, 0x00, 0x1D,  # Data size
    0x00, 0x00, 0x00, 0x00,  # Timestamp
    0x00, 0x00, 0x00,  # StreamID
    # This is a minimal example and not a valid video data.
])

# Seek Points (keyframe metadata)
seek_point_tag = bytes([
    0x09,  # Tag type video
    0x00, 0x00, 0x0A,  # Data size
    0x00, 0x00, 0x3C, 0x00,  # Timestamp in milliseconds (1000 ms)
    0x00, 0x00, 0x00,  # StreamID is always 0
])

# Screen Video Codec Tag
screen_video_codec_tag = bytes([
    0x09,  # Tag type video
    0x00, 0x00, 0x1E,  # Data size, adjust for actual data
    0x00, 0x00, 0x78, 0x00,  # Timestamp in milliseconds (3000 ms)
    0x00, 0x00, 0x00,  # StreamID
    0x02,  # CodecID for Screen Video (Assuming 0x02 for Screen Video Codec for illustration)
    # Screen Video Frame data would follow here
])

# Looping Support Tag (custom implementation, as FLV does not natively support looping metadata)
# For demonstration, we'll use a script tag with custom data indicating loop start and end points.
# In a real implementation, this would require a custom player that understands this tag.
loop_support_tag = bytes([
    0x12,  # Tag type script (metadata)
    0x00, 0x00, 0x29,  # Data size, adjust according to actual metadata size
    0x00, 0x00, 0x00, 0x00,  # Timestamp
    0x00, 0x00, 0x00,  # StreamID
    # Custom loop metadata would follow here, for example:
    # Loop start point, loop end point, flag to enable looping, etc.
    # This is purely illustrative and not functional without a custom player.
])

# Write the FLV content to a file
with open(output_path, 'wb') as f:
    f.write(flv_header)
    f.write(video_tag)
    f.write(seek_point_tag)
    f.write(screen_video_codec_tag)
    f.write(loop_support_tag)
    # Write a final PreviousTagSize to indicate end of file (Optional)
    # This PreviousTagSize should match the last tag's size, adjust accordingly.
    f.write(bytes([0x00, 0x00, 0x00, 0x29]))

print(f"Generated FLV file with Looping Support at: {output_path}")