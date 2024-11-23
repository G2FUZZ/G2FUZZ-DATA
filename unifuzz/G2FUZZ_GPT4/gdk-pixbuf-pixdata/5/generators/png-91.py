from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

def create_directory(directory_path):
    os.makedirs(directory_path, exist_ok=True)

def generate_gradient_image(width, height):
    image = Image.new("RGB", (width, height))
    for x in range(width):
        for y in range(height):
            gray = int((x / width) * 255)
            image.putpixel((x, y), (gray, gray, gray))
    return image

def apply_gamma_correction(image, gamma):
    gamma_correction = [int((i / 255.0) ** (1.0 / gamma) * 255) for i in range(256)]
    return image.point(gamma_correction * 3)

def add_text_watermark(image, text, position, font, fill):
    draw = ImageDraw.Draw(image)
    draw.text(position, text, font=font, fill=fill)
    return image

def rotate_image(image, angle):
    return image.rotate(angle, expand=True)

def apply_blur_filter(image, radius):
    return image.filter(ImageFilter.GaussianBlur(radius))

# Ensure the ./tmp/ directory exists
create_directory('./tmp/')

# Create a new image with RGB mode
width, height = 256, 256
image = generate_gradient_image(width, height)

# Apply gamma correction
gamma = 2.2
image = apply_gamma_correction(image, gamma)

# Rotate the image
angle = 45
image = rotate_image(image, angle)

# Apply blur filter
radius = 2
image = apply_blur_filter(image, radius)

# Adding a text watermark
text = "Sample Watermark"
position = (10, height - 30)  # Bottom left corner
# Ensure you have the font file accessible or use a basic font for demonstration
try:
    font = ImageFont.truetype("arial.ttf", 20)
except IOError:
    font = ImageFont.load_default()
fill = (255, 0, 0)  # Red color
image = add_text_watermark(image, text, position, font, fill)

# Save the image with gamma information
output_path = './tmp/complex_image.png'
image.save(output_path, "PNG", gamma=1.0/gamma)

print(f"Complex image with multiple enhancements saved to {output_path}")