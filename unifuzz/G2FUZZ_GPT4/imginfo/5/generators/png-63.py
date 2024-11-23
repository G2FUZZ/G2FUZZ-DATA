from PIL import Image, ImageDraw, ImageSequence, PngImagePlugin
import numpy as np
import os

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

def create_rgba_image_with_transparency():
    width, height = 100, 100
    array = np.linspace(0, 255, width * height)
    grey_scale = np.reshape(array, (height, width)).astype('uint8')
    alpha = np.linspace(0, 255, width * height)  # Gradient transparency
    alpha = np.reshape(alpha, (height, width)).astype('uint8')
    rgba_image = np.dstack((grey_scale, grey_scale, grey_scale, alpha))
    image_rgba = Image.fromarray(rgba_image, 'RGBA')
    image_rgba.save('./tmp/rgba_with_transparency.png')

def create_animated_png():
    images = []
    for i in range(5):  # Create 5 frames
        img = Image.new("RGBA", (100, 100), (255, 0, 0, 255))
        d = ImageDraw.Draw(img)
        d.text((10, 10), f"Frame {i}", fill=(255, 255, 255, 128))
        images.append(img)
    images[0].save('./tmp/animated.png', save_all=True, append_images=images[1:], loop=0, duration=200)

def embed_text_metadata():
    img = Image.new("RGB", (100, 100), "blue")
    meta = PngImagePlugin.PngInfo()
    meta.add_text("Author", "John Doe")
    meta.add_text("Description", "This is an example image with embedded text metadata.")
    img.save('./tmp/image_with_metadata.png', pnginfo=meta)

# Call the functions to create images
create_rgba_image_with_transparency()
create_animated_png()
embed_text_metadata()

print("Images with complex features have been generated.")