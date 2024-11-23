from PIL import Image

def generate_jpeg_with_compression(output_path, quality):
    # Ensure the output directory exists
    import os
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Create an image with a solid color (e.g., blue)
    # Image size is 800x600 pixels
    img = Image.new('RGB', (800, 600), color = (73, 109, 137))
    
    # Save the image with customizable compression level
    img.save(output_path, 'JPEG', quality=quality)

# Example usage
generate_jpeg_with_compression('./tmp/custom_compression_quality_70.jpg', quality=70)
generate_jpeg_with_compression('./tmp/custom_compression_quality_90.jpg', quality=90)