from PIL import Image, ImageDraw

def create_icon(size):
    # Create a new image with a white background
    image = Image.new("RGBA", (size, size), "white")
    draw = ImageDraw.Draw(image)
    
    # Draw a simple shape, for example, a circle in the center
    # Colors are chosen to make the icon colorful and stand out
    radius = size // 2 - 5  # Keeping some padding
    left_up_point = (5, 5)
    right_down_point = (size - 5, size - 5)
    draw.ellipse([left_up_point, right_down_point], fill='blue', outline='red')
    
    return image

def save_icon(filename, sizes=(16, 32, 48, 64, 128, 256)):
    # Create a list to hold the icons
    icons = [create_icon(size) for size in sizes]
    
    # Save the icons as a single .ico file
    icons[0].save(filename, format='ICO', sizes=[(size, size) for size in sizes])

# Ensure the ./tmp/ directory exists
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Save the ICO file with the desired sizes
save_icon('./tmp/versatile_icon.ico')