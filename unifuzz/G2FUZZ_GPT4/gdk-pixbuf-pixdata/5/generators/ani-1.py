import os
from PIL import Image, ImageDraw
import struct

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

def create_frame(image_size, color):
    """Create an individual frame for the animation."""
    frame = Image.new('RGBA', image_size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(frame)
    draw.ellipse((0, 0, image_size[0], image_size[1]), fill=color)
    return frame

def write_ani_file(file_path, frames, durations):
    """Generate and write the ANI file with the given frames and durations."""
    # Initial incorrect header packing
    # header = struct.pack('4sIIIIIIII', b'RIFF', 0, b'ACON', b'LIST', 0, b'fram', b'anih', 36, 36)
    
    # Corrected header packing
    # Note: The strings b'ACON', b'LIST', b'fram', b'anih' are now correctly placed outside the struct.pack call for integers.
    header_prefix = b'RIFF' + struct.pack('I', 0) + b'ACON' + b'LIST'
    header_suffix = struct.pack('I', 0) + b'fram' + b'anih' + struct.pack('II', 36, 36)
    header = header_prefix + header_suffix
    
    anih = struct.pack('IIIIIIIIII', 36, 36, len(frames), len(frames), 0, 0, 0, 0, 0, 0)
    rate = struct.pack('4sI' + 'I'*len(durations), b'rate', len(durations)*4, *durations)
    seq = struct.pack('4sII', b'seq ', 4, 0)
    ico_data = b''.join([frame.tobytes('raw', 'RGBA') for frame in frames])
    
    # Calculate sizes
    list_size = len(anih) + len(rate) + len(seq) + len(ico_data)
    file_size = 4 + 4 + 4 + 4 + list_size  # Correct calculation for the header size
    
    # Update sizes in header
    header_prefix = b'RIFF' + struct.pack('I', file_size) + b'ACON' + b'LIST'
    header_suffix = struct.pack('I', list_size) + b'fram' + b'anih' + struct.pack('II', 36, 36)
    header = header_prefix + header_suffix
    
    with open(file_path, 'wb') as f:
        f.write(header + anih + rate + seq + ico_data)

image_size = (32, 32)  # Size of the cursor images
colors = [(255, 0, 0, 255), (0, 255, 0, 255), (0, 0, 255, 255)]  # Red, Green, Blue frames
frames = [create_frame(image_size, color) for color in colors]
durations = [100, 100, 100]  # Frame durations in milliseconds

write_ani_file('./tmp/animated_cursor.ani', frames, durations)