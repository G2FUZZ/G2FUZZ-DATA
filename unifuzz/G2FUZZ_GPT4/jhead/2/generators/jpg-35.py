from PIL import Image
import os

def generate_gradient_image(width, height, start_color, end_color):
    """
    Generate a horizontal gradient image with given start and end colors.
    """
    image = Image.new("RGB", (width, height), "#FFFFFF")
    for x in range(width):
        for y in range(height):
            # Interpolate the RGB values
            r = int(start_color[0] + (float(x) / (width - 1)) * (end_color[0] - start_color[0]))
            g = int(start_color[1] + (float(x) / (width - 1)) * (end_color[1] - start_color[1]))
            b = int(start_color[2] + (float(x) / (width - 1)) * (end_color[2] - start_color[2]))
            image.putpixel((x, y), (r, g, b))
    return image

def save_image_with_huffman_coding(image, file_path):
    """
    Save the image using Huffman coding as part of JPEG compression.
    Note: The Huffman coding step is implicitly handled by the JPEG encoder.
    """
    if not os.path.exists(os.path.dirname(file_path)):
        os.makedirs(os.path.dirname(file_path))
    
    image.save(file_path, "JPEG")

def generate_and_save_gradients():
    # Define color gradients
    gradients = [
        ((0, 0, 0), (255, 0, 0), "red"),
        ((0, 0, 0), (0, 255, 0), "green"),
        ((0, 0, 0), (0, 0, 255), "blue"),
        ((0, 0, 0), (255, 255, 0), "yellow"),
    ]

    for start_color, end_color, color_name in gradients:
        img = generate_gradient_image(256, 256, start_color, end_color)
        
        # Create a directory path that includes the color name
        directory_path = f"./tmp/gradients/{color_name}"
        file_path = os.path.join(directory_path, f"gradient_{color_name}_huffman.jpg")
        
        save_image_with_huffman_coding(img, file_path)

if __name__ == "__main__":
    generate_and_save_gradients()