import os
from PIL import Image, ImageDraw

# Ensure the './tmp/' directory exists
output_dir = "./tmp"
os.makedirs(output_dir, exist_ok=True)

# Function to save an image (this is a simplified example for demonstration)
def save_image(img, filename):
    # Define the full path where the image will be saved
    filepath = os.path.join(output_dir, filename)
    
    # Save the image
    img.save(filepath)
    print(f"Image saved at {filepath}")

# Example usage
if __name__ == "__main__":
    # Create a simple image
    img = Image.new('RGB', (100, 100), color = (73, 109, 137))
    
    # Specify the filename
    filename = "example_image.jpg"
    
    # Save the image using the function
    save_image(img, filename)