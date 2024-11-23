from PIL import Image, ImageDraw
import os

# Create the tmp directory if it doesn't already exist
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Define the icon sizes for backward compatibility and newer systems
icon_sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]

# Create an image list to store different sizes for the ICO
images = []

for size in icon_sizes:
    # Create a new image with RGBA mode (to support alpha transparency)
    image = Image.new("RGBA", size, (255, 255, 255, 0))
    
    # Draw a simple shape to demonstrate backward compatibility with PNG compression & alpha transparency
    draw = ImageDraw.Draw(image)
    # Draw a circle that fills the image to test both features
    circle_radius = min(size) // 2 - 5
    draw.ellipse((5, 5, 5 + circle_radius * 2, 5 + circle_radius * 2), fill=(255, 0, 0, 127), outline=(0, 0, 0, 255))
    
    # Add the image to the list
    images.append(image)

# Save the images in the ICO format, including all sizes for backward compatibility
icon_path = os.path.join(output_dir, "test_icon.ico")
images[0].save(icon_path, format='ICO', sizes=[(s.width, s.height) for s in images])

print(f"ICO file with backward compatibility and newer features saved to: {icon_path}")