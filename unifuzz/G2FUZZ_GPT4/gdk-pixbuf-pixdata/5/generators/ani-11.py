import os
from PIL import Image, ImageDraw

# Create the tmp directory if it does not exist
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Function to create an icon image
def create_icon_image(size=(32, 32), color=(0, 0, 255, 0)):
    """
    Creates a simple square image with the specified size and color.

    :param size: A tuple representing the width and height of the image.
    :param color: A tuple representing the RGBA color of the square.
    :return: An Image object.
    """
    image = Image.new('RGBA', size)
    draw = ImageDraw.Draw(image)
    draw.rectangle([0, 0, size[0], size[1]], fill=color)
    return image

# Function to create an ANI file from a series of icon images
def create_ani_file(filename, frames, frame_rate=60):
    """
    Creates an ANI file from a list of Image objects.

    :param filename: The name of the ANI file to create.
    :param frames: A list of PIL Image objects to include in the ANI file.
    :param frame_rate: The frame rate for the animation.
    """
    # ANI header and other required bytes for a minimal ANI structure
    # This is a simplified example and does not cover all ANI aspects
    ani_header = b'RIFF\x00\x00\x00\x00ACONanih\x24\x00\x00\x00' + \
                 frame_rate.to_bytes(4, 'little') + \
                 len(frames).to_bytes(4, 'little') + \
                 (0).to_bytes(4, 'little') + \
                 (0).to_bytes(4, 'little') * 4

    # Create the ANI file and write the header
    with open(f'./tmp/{filename}', 'wb') as ani_file:
        ani_file.write(ani_header)

        # Write each frame as an ICO
        for frame in frames:
            # ICO files usually begin with a 6-byte header followed by image data
            # This is a highly simplified representation
            ico_header = b'\x00\x00\x01\x00\x01\x00' + \
                         frame.size[0].to_bytes(1, 'little') + \
                         frame.size[1].to_bytes(1, 'little') + \
                         (0).to_bytes(2, 'little') + \
                         (1).to_bytes(2, 'little') + \
                         (32).to_bytes(2, 'little') + \
                         (len(frame.tobytes()) + 40).to_bytes(4, 'little') + \
                         (22).to_bytes(4, 'little')  # Offset to image data, simplified

            # Write the ICO header
            ani_file.write(ico_header)
            # Write the image data
            frame.save(ani_file, format='PNG')

# Example usage
if __name__ == "__main__":
    # Generate a few simple frames
    frames = [create_icon_image(color=(255, 0, 0, 0)), create_icon_image(color=(0, 255, 0, 0)),
              create_icon_image(color=(0, 0, 255, 0))]

    # Create the ANI file
    create_ani_file('example.ani', frames)