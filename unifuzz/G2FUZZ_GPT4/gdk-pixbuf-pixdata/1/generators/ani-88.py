from PIL import Image
import os
import struct
from io import BytesIO

def create_frame(color, size=(32, 32)):
    """
    Create a single frame with the specified color and size.
    """
    image = Image.new("RGBA", size, color)
    return image

def write_ani_header(fp, num_frames, jif_rate):
    """
    Write the RIFF header and anih chunk for an ANI file.
    """
    # RIFF header
    fp.write(b'RIFF')
    # Placeholder for file size, will be updated later
    fp.write(struct.pack('<I', 0))
    fp.write(b'ACON')

    # anih chunk (header)
    fp.write(b'anih')
    anih_size = 36
    fp.write(struct.pack('<I', anih_size))
    
    # anih chunk content
    header_data = struct.pack('<IIIIIIII',
                              36,         # cbSize of anih structure
                              num_frames, # cFrames
                              num_frames, # cSteps
                              0,          # cx, cy (reserved, 0)
                              0,          # cBitCount (reserved, 0)
                              0,          # cPlanes (reserved, 0)
                              jif_rate,   # iDispRate (display rate in jiffies)
                              0           # flags
                              )
    fp.write(header_data)

def write_frame_icon(fp, image):
    """
    Write a frame as an ICON chunk.
    """
    # Convert the PIL image to ICO format and get bytes
    with BytesIO() as icon_io:
        image.save(icon_io, format='ICO', sizes=[image.size])
        icon_data = icon_io.getvalue()

    # Write LIST chunk for frame
    fp.write(b'LIST')
    list_size_pos = fp.tell()
    fp.write(struct.pack('<I', 0)) # Placeholder for list chunk size
    fp.write(b'fram')

    # Write icon data
    frame_data_size = len(icon_data)
    fp.write(icon_data)

    # Update LIST chunk size
    current_pos = fp.tell()
    list_chunk_size = current_pos - list_size_pos - 4
    fp.seek(list_size_pos)
    fp.write(struct.pack('<I', list_chunk_size))
    fp.seek(current_pos)

def save_ani(frames, filename, frame_rate=60):
    """
    Save a sequence of frames as an .ani file.
    """
    # Ensure the tmp directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    jif_rate = int(1000 / frame_rate)  # Convert frame rate to jiffies (1/60th of a second)
    num_frames = len(frames)

    with open(filename, 'wb') as fp:
        write_ani_header(fp, num_frames, jif_rate)

        for frame in frames:
            write_frame_icon(fp, frame)

        # Update file size in RIFF header
        file_size = fp.tell() - 8  # Total file size minus RIFF header size
        fp.seek(4)
        fp.write(struct.pack('<I', file_size))

# Example usage
if __name__ == "__main__":
    # Generate a sequence of frames with different colors
    colors = ["red", "green", "blue", "yellow"]
    frames = [create_frame(color) for color in colors]

    # Save the sequence as an .ani file
    save_ani(frames, "./tmp/animation.ani", frame_rate=60)