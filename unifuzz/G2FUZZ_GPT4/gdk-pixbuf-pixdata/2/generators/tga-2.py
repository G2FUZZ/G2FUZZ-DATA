from PIL import Image

def create_tga_with_alpha_channel(filename, size=(100, 100), color=(255, 0, 0, 128)):
    """
    Create a TGA file with an alpha channel.

    :param filename: Name of the file to save, without the path.
    :param size: Tuple of the image size, default is 100x100.
    :param color: Tuple of the RGBA color, default is semi-transparent red.
    """
    # Ensure the 'tmp' directory exists
    import os
    dir_path = './tmp/'
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    # Create a new image with RGBA (Red, Green, Blue, Alpha) mode
    image = Image.new('RGBA', size, color)

    # Save the image as TGA
    image.save(f'{dir_path}{filename}', 'TGA')

# Example usage
create_tga_with_alpha_channel('example_with_alpha.tga')