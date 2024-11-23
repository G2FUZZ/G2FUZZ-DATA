from PIL import Image, ImageDraw

def create_image(width, height, color):
    """Create an image with the given color."""
    image = Image.new("RGB", (width, height), color)
    return image

def merge_images(image1, image2):
    """Merge two images side by side."""
    total_width = image1.width + image2.width
    max_height = max(image1.height, image2.height)
    
    new_image = Image.new('RGB', (total_width, max_height))
    new_image.paste(image1, (0, 0))
    new_image.paste(image2, (image1.width, 0))
    
    return new_image

def main():
    # Create a main image and a thumbnail
    main_image = create_image(800, 600, "blue")
    thumbnail = create_image(200, 150, "red")
    
    # Merge the main image and thumbnail side by side
    merged_image = merge_images(main_image, thumbnail)
    
    # Ensure the ./tmp/ directory exists
    import os
    os.makedirs("./tmp/", exist_ok=True)
    
    # Save the merged image as a TGA file
    merged_image.save("./tmp/merged_image.tga")

if __name__ == "__main__":
    main()