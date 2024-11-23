from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

# Create a new image with multiple text overlays, shapes, and gradients
def create_complex_image(width, height, background_color, text_list, shape, gradient_colors):
    image = Image.new('RGB', (width, height), background_color)
    draw = ImageDraw.Draw(image)
    
    # Use a system font
    font = ImageFont.load_default()

    # Add text overlays
    for idx, text in enumerate(text_list):
        text_width, text_height = draw.textsize(text, font)
        text_position = ((width - text_width) // 2, (height // len(text_list)) * idx)
        draw.text(text_position, text, font=font, fill='white')

    # Add shapes
    if shape == 'circle':
        draw.ellipse((10, 10, width - 10, height - 10), outline='red')
    elif shape == 'rectangle':
        draw.rectangle((20, 20, width - 20, height - 20), outline='green')

    # Add gradient
    for y in range(height):
        draw.line((0, y, width, y), fill=gradient_colors[y], width=1)

    return image

# Save the image with different quality settings and complex structures
text_list = ['Hello', 'World', 'PIL']
gradient_colors = [(255, i, 0) for i in range(256)]  # Red to Yellow gradient

for quality in range(50, 100, 10):
    file_path = f'./tmp/complex_image_quality_{quality}.jpg'
    image = create_complex_image(200, 200, 'lightblue', text_list, 'rectangle', gradient_colors)
    image = image.filter(ImageFilter.GaussianBlur(radius=2))  # Apply Gaussian blur
    image.save(file_path, quality=quality)

print("JPG files with variable quality settings and complex structures saved successfully.")