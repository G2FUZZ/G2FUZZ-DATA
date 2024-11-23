from PIL import Image, ImageDraw
import os
import struct

def create_frame(size, color):
    """Create a single frame with specified size and color."""
    image = Image.new("RGBA", size, color)
    draw = ImageDraw.Draw(image)
    # Draw a simple shape
    draw.ellipse((size[0]//4, size[1]//4, 3*size[0]//4, 3*size[1]//4), fill=(255,255,255,255))
    return image

def save_ani(frames, file_path, frame_rates):
    """Save frames as an ANI file with specified frame rates."""
    with open(file_path, 'wb') as f:
        # ANI header
        f.write(b'RIFF')  # ChunkID
        f.write(struct.pack('<I', 36 + sum(len(frame.tobytes()) + 16 for frame in frames)))  # ChunkSize
        f.write(b'ACON')  # Format

        # ANIH chunk
        f.write(b'anih')  # ChunkID
        f.write(struct.pack('<I', 36))  # ChunkSize
        f.write(struct.pack('<I', 36))  # cbSizeOf
        f.write(struct.pack('<I', len(frames)))  # cFrames
        f.write(struct.pack('<I', len(frames)))  # cSteps
        f.write(struct.pack('<I', 0))  # cx, cy (0 for variable resolution)
        f.write(struct.pack('<I', 0))  # cBitCount, cPlanes
        f.write(struct.pack('<I', 0))  # JifRate
        f.write(struct.pack('<I', 0))  # Flags

        # RATE chunk (optional)
        f.write(b'rate')  # ChunkID
        f.write(struct.pack('<I', len(frame_rates) * 4))  # ChunkSize
        for rate in frame_rates:
            f.write(struct.pack('<I', rate))  # JifRate for each frame

        # SEQ chunk (optional)
        # Skipping for simplicity, would define sequence of frames

        # ICONS
        for frame in frames:
            f.write(b'icon')  # ChunkID
            frame_data = frame.tobytes()
            f.write(struct.pack('<I', len(frame_data) + 16))  # ChunkSize
            f.write(struct.pack('<I', frame.width))
            f.write(struct.pack('<I', frame.height))
            f.write(struct.pack('<I', 0))  # Colors (0 = no palette)
            f.write(struct.pack('<I', len(frame_data)))  # Bits size
            f.write(frame_data)

# Create frames with variable resolution
frames = [create_frame((32, 32), "red"), create_frame((64, 64), "blue")]

# Ensure tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Save the ANI file
save_ani(frames, './tmp/variable_resolution.ani', [10, 20])