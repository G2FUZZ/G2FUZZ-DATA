import os
from PIL import Image, ImageDraw

# Create the target directory if it doesn't exist
target_dir = "./tmp/"
os.makedirs(target_dir, exist_ok=True)

# Define the sizes for the icons
sizes = [(16, 16), (32, 32), (48, 48), (64, 64)]

# Create a list to hold the images
icons = []

for size in sizes:
    # Create a new image with a white background
    image = Image.new("RGBA", size, (255, 255, 255, 0))

    # Get a drawing context
    draw = ImageDraw.Draw(image)

    # Draw a simple shape that varies with size for demonstration
    # Here, we draw a circle that fills the image
    draw.ellipse((0, 0, size[0] - 1, size[1] - 1), fill='blue', outline='red')

    # Add the image to the list of icons
    icons.append(image)

# Save the icons into an .ico file
ico_path = os.path.join(target_dir, "generated_icon.ico")
icons[0].save(ico_path, format='ICO', sizes=[(icon.width, icon.height) for icon in icons])