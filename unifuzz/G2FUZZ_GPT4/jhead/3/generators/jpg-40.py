from PIL import Image, ImageDraw, ImageFilter, ImageFont
import numpy as np
import os

def generate_radial_gradient_image(width, height, start_color, end_color):
    base = np.zeros((height, width, 3), dtype=np.uint8)
    center_x, center_y = width // 2, height // 2
    for x in range(width):
        for y in range(height):
            distance = np.sqrt((center_x - x) ** 2 + (center_y - y) ** 2)
            max_dist = np.sqrt(center_x ** 2 + center_y ** 2)
            factor = distance / max_dist
            color = (1 - factor) * np.array(start_color) + factor * np.array(end_color)
            base[y, x] = color
    return base

def add_text_overlay(image_array, text, position, font_path=None, font_size=30, font_color=(255, 255, 255)):
    image = Image.fromarray(image_array)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_path, font_size) if font_path else ImageFont.load_default()
    draw.text(position, text, fill=font_color, font=font)
    return np.array(image)

def apply_blur_effect(image_array, radius=5):
    image = Image.fromarray(image_array)
    blurred_image = image.filter(ImageFilter.GaussianBlur(radius))
    return np.array(blurred_image)

def save_image_with_compression(image_array, path, compression_level):
    image = Image.fromarray(np.uint8(image_array))
    image.save(path, quality=compression_level)

def main():
    os.makedirs('./tmp/', exist_ok=True)
    width, height = 800, 600
    start_color, end_color = (0, 0, 128), (255, 255, 0)
    image_array = generate_radial_gradient_image(width, height, start_color, end_color)
    text = "Hello, World!"
    position = (width // 4, height // 2)
    image_array_with_text = add_text_overlay(image_array, text, position)
    blurred_image_array = apply_blur_effect(image_array_with_text, radius=2)
    compression_levels = [95, 50, 10]
    for level in compression_levels:
        filename = f'./tmp/complex_gradient_compression_{level}.jpg'
        save_image_with_compression(blurred_image_array, filename, level)
    print("Complex images have been saved with different compression levels.")

if __name__ == "__main__":
    main()