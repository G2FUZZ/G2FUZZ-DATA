from PIL import Image, ImageDraw
import os

def create_ani_file(file_path, hotspot=(0, 0), frames_count=10, frame_dimensions=(32, 32), frame_rate=10):
    # Ensure the tmp directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # ANI header structure
    RIFF = b'RIFF'
    ACON = b'ACON'
    LIST = b'LIST'
    INAM = b'INAM'
    IART = b'ART '
    RATE = b'rate'
    fram = b'fram'
    ICON = b'icon'
    anih = b'anih'
    
    # Creating a simple frame for demonstration
    def create_frame(dimensions, color):
        img = Image.new("RGBA", dimensions, color)
        draw = ImageDraw.Draw(img)
        # Draw a simple element, here a rectangle
        draw.rectangle([dimensions[0]//4, dimensions[1]//4, 3*dimensions[0]//4, 3*dimensions[1]//4], fill="red")
        return img
    
    frames = [create_frame(frame_dimensions, "white") for _ in range(frames_count)]
    frame_bytes = [b''] * frames_count
    
    for i, frame in enumerate(frames):
        # Convert PIL image to bytes
        with open(f"./tmp/frame_{i}.ico", "wb") as ico_file:
            frame.save(ico_file, format="ICO", sizes=[frame_dimensions])
        with open(f"./tmp/frame_{i}.ico", "rb") as ico_file:
            frame_bytes[i] = ico_file.read()
        os.remove(f"./tmp/frame_{i}.ico")
    
    # ANI file construction
    with open(file_path, "wb") as f:
        f.write(RIFF)
        f.write((36 + sum(len(fb) for fb in frame_bytes)).to_bytes(4, byteorder="little"))
        f.write(ACON)
        f.write(LIST)
        f.write((16).to_bytes(4, byteorder="little"))
        f.write(anih)
        f.write((36).to_bytes(4, byteorder="little"))  # anih size
        f.write((36).to_bytes(4, byteorder="little"))  # cbSize
        f.write(frames_count.to_bytes(4, byteorder="little"))  # cFrames
        f.write(frames_count.to_bytes(4, byteorder="little"))  # cSteps
        f.write((0).to_bytes(4, byteorder="little"))  # cx, cy (reserved, must be zero)
        f.write((0).to_bytes(4, byteorder="little"))  # cBitCount, cPlanes (reserved, must be zero)
        f.write((frame_rate).to_bytes(4, byteorder="little"))  # JifRate
        f.write((1).to_bytes(4, byteorder="little"))  # flags
        f.write(fram)
        f.write((sum(len(fb) for fb in frame_bytes) + 8).to_bytes(4, byteorder="little"))
        f.write(ICON)
        for fb in frame_bytes:
            f.write(fb)

# Specify the path and hotspot for the ani file
file_path = "./tmp/cursor.ani"
hotspot = (16, 16)  # Center for 32x32 cursor
create_ani_file(file_path, hotspot=hotspot)