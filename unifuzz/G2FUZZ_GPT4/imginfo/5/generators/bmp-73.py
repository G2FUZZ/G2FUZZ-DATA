from PIL import Image, ImageDraw, ImageFont
import os

def create_directory(path):
    # Ensure the directory exists
    os.makedirs(path, exist_ok=True)

def draw_shapes_and_text(image):
    draw = ImageDraw.Draw(image)
    
    # Draw a rectangle (start_x, start_y, end_x, end_y)
    draw.rectangle([20, 20, 80, 80], outline="red", fill=None)
    
    # Draw a circle (center_x, center_y, radius)
    # PIL expects a bounding box: top-left and bottom-right corners.
    draw.ellipse([25, 25, 75, 75], outline="green", fill=None)
    
    # Add text
    try:
        font = ImageFont.truetype("arial.ttf", 15)
    except IOError:
        font = ImageFont.load_default()
    
    draw.text((10, 10), "Hello", fill="white", font=font)

def blend_images(base_image):
    # Create a new image for blending
    blend_image = Image.new('RGB', base_image.size, 'magenta')
    blended = Image.blend(base_image, blend_image, alpha=0.5)
    return blended

def main():
    # Ensure the ./tmp/ directory exists
    create_directory('./tmp/')
    
    # Create a new image with width=100, height=100
    width, height = 100, 100
    base_image = Image.new('RGB', (width, height), 'blue')
    
    # Draw shapes and text on the image
    draw_shapes_and_text(base_image)
    
    # Blend the base image with another image
    final_image = blend_images(base_image)
    
    # Save the image as BMP
    file_path = './tmp/complex_image.bmp'
    final_image.save(file_path)
    
    print(f"Image saved to {file_path}")

if __name__ == "__main__":
    main()