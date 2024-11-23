from PIL import Image, ImageDraw, ImageFont
import os

# Function to create an image with more complex features
def create_complex_image(filename, image_size, background_color, text, text_color, shape, shape_color, quality, optimize=False):
    # Create a new image with the specified background color
    image = Image.new("RGB", image_size, background_color)
    
    # Initialize ImageDraw to draw on the image
    draw = ImageDraw.Draw(image)
    
    # Draw a shape on the image
    if shape == "rectangle":
        # Draw a rectangle
        draw.rectangle([10, 10, image_size[0]-10, image_size[1]-10], outline=shape_color, width=3)
    elif shape == "ellipse":
        # Draw an ellipse
        draw.ellipse([10, 10, image_size[0]-10, image_size[1]-10], outline=shape_color, width=3)
    
    # Add text to the image
    try:
        font = ImageFont.truetype("arial.ttf", 15)
    except IOError:
        # Fallback to default font if specific font is not found
        font = ImageFont.load_default()
    
    text_width, text_height = draw.textsize(text, font=font)
    text_position = ((image_size[0] - text_width) / 2, (image_size[1] - text_height) / 2)
    draw.text(text_position, text, fill=text_color, font=font)
    
    # Save the image with specified quality and optimization
    image.save(filename, "JPEG", quality=quality, optimize=optimize)
    print(f"Saved {filename} with compression level {quality}, optimize={optimize}")

# Ensure the ./tmp/ directory exists
os.makedirs("./tmp/", exist_ok=True)

# Parameters for creating complex images
sizes = [(100, 100), (200, 150), (300, 200)]
background_colors = ["blue", "green", "purple"]
texts = ["Hello", "World", "Complex"]
text_colors = ["white", "yellow", "black"]
shapes = ["rectangle", "ellipse"]
shape_colors = ["red", "orange", "cyan"]
compression_levels = [10, 50, 95]
optimize_flag = [False, True]

# Generate images with various combinations of the above parameters
for size in sizes:
    for background_color in background_colors:
        for text, text_color in zip(texts, text_colors):
            for shape, shape_color in zip(shapes, shape_colors):
                for quality in compression_levels:
                    for optimize in optimize_flag:
                        filename = f"./tmp/complex_{size[0]}x{size[1]}_{background_color}_{text}_{quality}_opt{optimize}.jpg"
                        create_complex_image(filename, size, background_color, text, text_color, shape, shape_color, quality, optimize)