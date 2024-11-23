from PIL import Image, ImageDraw, ImageFont
import os

def create_image(directory, filename, size=(600, 400)):
    """
    Creates an image with complex structures including circles, rectangles, text, and lines with multiple colors.
    Saves the image in the specified directory with the given filename.
    """
    # Ensure the directory exists
    os.makedirs(directory, exist_ok=True)
    
    # Create a new image with a white background
    image = Image.new('RGB', size, 'white')
    draw = ImageDraw.Draw(image)

    # Draw rectangles
    draw.rectangle([50, 50, 250, 150], outline="blue", fill="lightblue")
    draw.rectangle([350, 50, 550, 150], outline="green", fill="lightgreen")

    # Draw circles (ellipses with equal width and height)
    draw.ellipse([100, 200, 200, 300], outline="red", fill="pink")
    draw.ellipse([400, 200, 500, 300], outline="purple", fill="lavender")

    # Draw lines
    draw.line([300, 0, 300, 400], fill="gray", width=2)
    draw.line([0, 200, 600, 200], fill="gray", width=2)

    # Prepare to draw text
    try:
        # Use a truetype font if available
        font = ImageFont.truetype("arial.ttf", 24)
    except IOError:
        # Fallback to a default font
        font = ImageFont.load_default()

    # Draw text
    draw.text((60, 160), "Hello", fill="darkblue", font=font)
    draw.text((360, 160), "World", fill="darkgreen", font=font)
    draw.text((100, 310), "Circle 1", fill="darkred", font=font)
    draw.text((400, 310), "Circle 2", fill="indigo", font=font)

    # Save the image
    full_path = os.path.join(directory, filename)
    image.save(full_path, 'JPEG')

    print(f"Image saved to {full_path}")

# Example usage
create_image('./tmp/', 'complex_test_image.jpg')