from PIL import Image, ImageDraw

# Function to create an image for a specific resolution
def create_image(size):
    # Create a new image with RGBA (Red, Green, Blue, Alpha transparency) mode
    image = Image.new("RGBA", (size, size), (255, 255, 255, 0))
    
    # Initialize the drawing context
    draw = ImageDraw.Draw(image)
    
    # Draw a simple shape - a circle in this case
    draw.ellipse((0, 0, size-1, size-1), fill="blue", outline="red")
    
    # Optionally, more complex drawing operations can be performed here
    
    return image

# Create images for different resolutions
sizes = [64, 128] # Define desired sizes here
images = [create_image(size) for size in sizes]

# Ensure the ./tmp/ directory exists
import os
os.makedirs("./tmp/", exist_ok=True)

# Save the images as an ICO file
ico_path = "./tmp/multi_resolution_icon.ico"
images[0].save(ico_path, format="ICO", sizes=[(size, size) for size in sizes])

print(f"ICO file with multiple resolutions saved at: {ico_path}")