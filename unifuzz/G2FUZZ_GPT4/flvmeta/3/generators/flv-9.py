import os

# Ensure the tmp directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Path to the output FLV file
output_path = os.path.join(output_dir, "example.flv")

# FLV file header and metadata for a video tag to simulate embedding capabilities
flv_header = bytes([
    0x46, 0x4C, 0x56,  # Signature "FLV"
    0x01,  # Version 1
    0x05,  # TypeFlags (audio + video)
    0x00, 0x00, 0x00, 0x09,  # DataOffset, FLV header length
    # FLV Body start
    0x00, 0x00, 0x00, 0x00  # PreviousTagSize0
])

# Sample video tag (minimal and not a valid video data, for demonstration only)
video_tag = bytes([
    0x12,  # Tag type script
    0x00, 0x00, 0x1D,  # Data size
    0x00, 0x00, 0x00, 0x00,  # Timestamp
    0x00, 0x00, 0x00,  # StreamID
    # Actual data would go here, but we're keeping it minimal.
    # For a real video, data representing frames and metadata would be included.
])

# Write the FLV content to a file
with open(output_path, 'wb') as f:
    f.write(flv_header)
    f.write(video_tag)
    # Write a final PreviousTagSize to indicate end of file (Optional)
    f.write(bytes([0x00, 0x00, 0x00, 0x1D]))

print(f"Generated FLV file at: {output_path}")