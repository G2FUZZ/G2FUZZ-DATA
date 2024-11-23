import os
from io import BytesIO
import struct

# Function to create a simple frame with variable dimensions
def create_frame(width, height):
    # Create a simple image (for demonstration, we fill it with a solid color)
    # Here, we're creating a simple bitmap (BMP) format image for each frame.
    image_data = bytearray([0] * (width * height * 3))
    for i in range(height):
        for j in range(width):
            index = (i * width + j) * 3
            image_data[index:index+3] = bytearray([i % 256, j % 256, (i+j) % 256])  # Example pattern
    bmp_header = bytearray([
        0x42, 0x4D,  # 'BM' signature
        0x36, 0x28, 0x00, 0x00,  # File size (dummy)
        0x00, 0x00,  # Reserved
        0x00, 0x00,  # Reserved
        0x36, 0x00, 0x00, 0x00,  # Offset to pixel data
        0x28, 0x00, 0x00, 0x00,  # Header size
        width & 0xFF, (width >> 8) & 0xFF, 0x00, 0x00,  # Image width
        height & 0xFF, (height >> 8) & 0xFF, 0x00, 0x00,  # Image height
        0x01, 0x00,  # Planes
        0x18, 0x00,  # Bits per pixel (24)
        0x00, 0x00, 0x00, 0x00,  # Compression (none)
        0x00, 0x28, 0x00, 0x00,  # Image size (dummy)
        0x00, 0x00, 0x00, 0x00,  # X pixels per meter (dummy)
        0x00, 0x00, 0x00, 0x00,  # Y pixels per meter (dummy)
        0x00, 0x00, 0x00, 0x00,  # Total colors
        0x00, 0x00, 0x00, 0x00   # Important colors
    ])
    return bmp_header + image_data

# Function to write an ANI file
def write_ani_file(frames, rates, file_path):
    with open(file_path, 'wb') as f:
        # RIFF header
        f.write(b'RIFF')
        f.write(struct.pack('<I', 0))  # Placeholder for file size
        f.write(b'ACON')

        # ANI header
        f.write(b'anih')
        f.write(struct.pack('<I', 36))  # Chunk size
        f.write(struct.pack('<I', 36))  # Header size
        f.write(struct.pack('<I', len(frames)))  # Number of frames
        f.write(struct.pack('<I', len(frames)))  # Number of steps
        f.write(struct.pack('<I', 0))  # Width (will be ignored)
        f.write(struct.pack('<I', 0))  # Height (will be ignored)
        f.write(struct.pack('<I', 0))  # Bit count (will be ignored)
        f.write(struct.pack('<I', len(frames)))  # Number of planes (will be ignored)
        f.write(struct.pack('<I', 0))  # Display rate (jiffies)
        f.write(struct.pack('<I', 0))  # Flags

        # RATE chunk (optional, but recommended)
        f.write(b'rate')
        f.write(struct.pack('<I', 4 * len(frames)))  # Chunk size
        for rate in rates:  # Write each rate
            f.write(struct.pack('<I', rate))

        # SEQ chunk (optional)
        # Not included in this example for simplicity

        # Frame data
        for frame in frames:
            frame_data = frame.getvalue()
            f.write(b'icon')
            f.write(struct.pack('<I', len(frame_data)))
            f.write(frame_data)

        # Update file size
        f.seek(4)
        f.write(struct.pack('<I', os.path.getsize(file_path) - 8))

# Generate frames with variable dimensions
frames = []
for i in range(1, 6):  # Generate 5 frames with increasing sizes
    frame_width, frame_height = i * 32, i * 32  # Variable dimensions
    frame_data = BytesIO(create_frame(frame_width, frame_height))
    frames.append(frame_data)

# Define display rates for each frame (in jiffies; 60 jiffies = 1 second)
rates = [60, 60, 60, 60, 60]

# Specify the path to save the ANI file
file_path = './tmp/variable_size.ani'

# Ensure the tmp directory exists
os.makedirs(os.path.dirname(file_path), exist_ok=True)

# Write the ANI file
write_ani_file(frames, rates, file_path)