from PIL import Image, ImageDraw
import os

def create_image_with_transparency(size, color, transparency):
    """Create an image with transparency."""
    image = Image.new("RGBA", size, color)
    alpha = Image.new("L", size, transparency)
    image.putalpha(alpha)
    return image

def create_ani_file(directory, file_name, frames, frame_rate):
    """Compile frames into an ANI file with 32-bit color support."""
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    with open(os.path.join(directory, file_name), "wb") as ani_file:
        # ANI header structure and default values for demonstration, might not be fully correct
        ani_header = b'RIFF\x00\x00\x00\xACONanih\x2c\x00\x00\x00\x24\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00' + \
                     frame_rate.to_bytes(4, byteorder='little') + \
                     b'\x00\x00\x00\x00LIST\x00\x00\x00\x00fram'
        
        ani_file.write(ani_header)
        
        for frame in frames:
            with open(frame, "rb") as frame_file:
                ani_file.write(frame_file.read())
        
        # This is a simplified example and might not produce a fully functional .ani file
        # as the .ani format requires specific structures and metadata.

def main():
    directory = './tmp/'
    file_name = 'example.ani'
    size = (32, 32)
    colors = [(255, 0, 0, 128), (0, 255, 0, 128), (0, 0, 255, 128)]
    frame_rate = 10  # 10 milliseconds
    frames = []

    # Generate frames with transparency
    for i, color in enumerate(colors):
        image = create_image_with_transparency(size, color, 128)
        frame_path = os.path.join(directory, f'frame_{i}.png')
        image.save(frame_path)
        frames.append(frame_path)

    # Create ANI file
    create_ani_file(directory, file_name, frames, frame_rate)

    # Cleanup individual frame files
    for frame in frames:
        os.remove(frame)

if __name__ == "__main__":
    main()