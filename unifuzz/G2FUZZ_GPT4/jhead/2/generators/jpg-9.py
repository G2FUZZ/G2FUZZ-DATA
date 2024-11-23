from PIL import Image
import os

def generate_gradient_image(width, height):
    """
    Generate a horizontal gradient image from black to white.
    """
    image = Image.new("RGB", (width, height), "#FFFFFF")
    for x in range(width):
        for y in range(height):
            # Calculate the intensity based on the x position
            intensity = int((x / (width - 1)) * 255)
            image.putpixel((x, y), (intensity, intensity, intensity))
    return image

def save_image_with_huffman_coding(image, file_path):
    """
    Save the image using Huffman coding as part of JPEG compression.
    Note: The Huffman coding step is implicitly handled by the JPEG encoder.
    """
    if not os.path.exists(os.path.dirname(file_path)):
        os.makedirs(os.path.dirname(file_path))
    
    image.save(file_path, "JPEG")

if __name__ == "__main__":
    # Generate a gradient image
    img = generate_gradient_image(256, 256)
    
    # Save the image with Huffman coding (JPEG compression)
    save_image_with_huffman_coding(img, "./tmp/gradient_huffman.jpg")