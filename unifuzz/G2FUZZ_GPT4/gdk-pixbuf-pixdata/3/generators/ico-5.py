from PIL import Image, ImageDraw

# Directory to save the generated .ico file
output_dir = "./tmp/"

# Ensuring the output directory exists
import os
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Function to create an image representing the feature
def create_feature_icon(size):
    # Create a new image with white background
    image = Image.new("RGBA", (size, size), "white")
    draw = ImageDraw.Draw(image)

    # Drawing a simple cross to symbolize compatibility
    draw.line((size * 0.2, size * 0.2, size * 0.8, size * 0.8), fill="black", width=int(size*0.1))
    draw.line((size * 0.8, size * 0.2, size * 0.2, size * 0.8), fill="black", width=int(size*0.1))

    # Optional: Add more elements to symbolize "universal choice" or "compatibility"
    # For simplicity, this example will stick with a simple design

    return image

# Sizes for the ICO file (standard sizes include 16x16, 32x32, 48x48, etc.)
icon_sizes = [16, 32, 48, 64, 128, 256]

# Create images for each size
icons = [create_feature_icon(size) for size in icon_sizes]

# Save the icons as a single .ico file
ico_path = os.path.join(output_dir, "feature_compatibility.ico")
icons[0].save(ico_path, format="ICO", sizes=[(icon.width, icon.height) for icon in icons])