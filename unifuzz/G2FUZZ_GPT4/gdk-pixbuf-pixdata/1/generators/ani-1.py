import os
from PIL import Image
import struct

def create_frame(color, size=(32, 32)):
    """Create a single image (frame) with the specified color."""
    image = Image.new("RGBA", size, color)
    return image

def frames_to_ani(frames, filename, rate=60):
    """Convert a list of PIL Images to a .ani file."""
    # ANI header structure: RIFF, ACON, list, INAM, IART, RATE, seq , and anil chunks
    # This is a very basic implementation and might not work in all cases.
    with open(filename, 'wb') as f:
        # Write the header
        f.write(b'RIFF')
        f.write(struct.pack('<I', 36 + 16*len(frames)))  # File size
        f.write(b'ACON')

        # Write the INFO LIST
        f.write(b'LIST')
        f.write(struct.pack('<I', 4))
        f.write(b'INFO')

        # Write the sequence
        f.write(b'seq ')
        f.write(struct.pack('<I', len(frames)))
        f.write(bytes(range(len(frames))))

        # Write the rate
        f.write(b'rate')
        f.write(struct.pack('<I', len(frames)*4))
        for _ in frames:
            f.write(struct.pack('<I', rate))  # Rate for each frame

        # Write frames
        for i, frame in enumerate(frames):
            frame_data = frame.tobytes()
            f.write(b'icon')
            f.write(struct.pack('<I', 16 + len(frame_data)))
            f.write(struct.pack('<I', 32))  # Width
            f.write(struct.pack('<I', 32))  # Height
            f.write(struct.pack('<I', 0))   # Colors
            f.write(struct.pack('<I', 0))   # Reserved
            f.write(struct.pack('<H', 1))   # Planes
            f.write(struct.pack('<H', 32))  # Bit count
            f.write(struct.pack('<I', len(frame_data)))  # Size of image data
            f.write(struct.pack('<I', 22 + 16*len(frames) + i*len(frame_data)))  # Offset of image data
            f.write(frame_data)

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate a series of frames
colors = [(255, 0, 0, 255), (0, 255, 0, 255), (0, 0, 255, 255), (255, 255, 0, 255)]
frames = [create_frame(color) for color in colors]

# Save frames to an ANI file
frames_to_ani(frames, './tmp/animation.ani')

print("ANI file generated successfully.")