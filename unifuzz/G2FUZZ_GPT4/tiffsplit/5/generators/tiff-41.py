from PIL import Image, ImageDraw, ImageCms
import numpy as np
import os

def create_gradient_image(size, color_stops):
    """Creates an image with a gradient."""
    width, height = size
    image = np.zeros((height, width, 4), dtype=np.uint8)  # RGBA
    for x in range(width):
        for y in range(height):
            r, g, b, a = color_stops
            image[y, x] = [255, x % r, y % g, int(a * (x / width))]
    return Image.fromarray(image, 'RGBA')

def add_text_to_image(image, text, position=(10, 10), color='white'):
    """Adds text to an image."""
    draw = ImageDraw.Draw(image)
    draw.text(position, text, fill=color)
    return image

def save_multi_page_tiff(output_path, images, icc_profiles, metadata_list):
    """Saves a list of images as a multi-page TIFF, each with its own ICC profile and metadata."""
    save_all = True
    append_images = []
    for i, img in enumerate(images[1:], start=1):
        output_img = ImageCms.profileToProfile(img, icc_profiles[i], icc_profiles[i], outputMode='RGB')
        if metadata_list and len(metadata_list) > i:
            output_img.info['Description'] = metadata_list[i]
        append_images.append(output_img)
    first_img = ImageCms.profileToProfile(images[0], icc_profiles[0], icc_profiles[0], outputMode='RGB')
    if metadata_list:
        first_img.info['Description'] = metadata_list[0]
    first_img.save(output_path, save_all=save_all, append_images=append_images, format='TIFF')

def main():
    os.makedirs('./tmp/', exist_ok=True)
    images = [
        create_gradient_image((300, 300), (256, 256, 256, 255)),
        create_gradient_image((350, 350), (256, 200, 200, 200)),
        create_gradient_image((400, 400), (200, 256, 200, 150))
    ]
    images = [add_text_to_image(img, f"Page {i+1}") for i, img in enumerate(images)]
    icc_profile = ImageCms.createProfile("sRGB")
    icc_profiles = [icc_profile for _ in images]
    metadata_list = [f"This is page {i+1}" for i in range(len(images))]
    output_path = './tmp/multi_page_alpha_channel_image.tiff'
    save_multi_page_tiff(output_path, images, icc_profiles, metadata_list)
    print("Multi-page TIFF image with alpha channel and ICC profiles saved successfully.")

if __name__ == "__main__":
    main()