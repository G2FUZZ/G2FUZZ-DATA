from PIL import Image, ImageDraw, ImageFont
import os

# Ensure ./tmp/ directory exists
os.makedirs("./tmp/complex/", exist_ok=True)

# Define a function to create a single image
def create_image(background_color, text, text_color, ellipse_color, image_size=(100, 100)):
    image = Image.new("RGB", image_size, background_color)
    draw = ImageDraw.Draw(image)
    
    # Draw an ellipse
    ellipse_bounds = [10, 10, 90, 50]  # Left, Top, Right, Bottom
    draw.ellipse(ellipse_bounds, fill=ellipse_color)
    
    # Load a font
    try:
        font_size = 20
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        print("Default font will be used due to missing 'arial.ttf'")
        font = ImageFont.load_default()
    
    # Add text
    text_position = (10, 60)
    draw.text(text_position, text, fill=text_color, font=font)
    
    return image

# Define grid size
grid_size = (2, 3)  # Rows, Columns

# Create a new image to hold the grid
grid_image_size = (grid_size[1] * 100, grid_size[0] * 100)
grid_image = Image.new("RGB", grid_image_size)

background_colors = ["blue", "green", "red", "purple", "yellow", "orange"]
text_colors = ["white", "black"]
ellipse_colors = ["white", "grey"]

# Iterate through the grid and create individual images
for row in range(grid_size[0]):
    for col in range(grid_size[1]):
        index = row * grid_size[1] + col
        background_color = background_colors[index % len(background_colors)]
        text_color = text_colors[index % len(text_colors)]
        ellipse_color = ellipse_colors[index % len(ellipse_colors)]
        
        # Create an individual image
        image = create_image(background_color, f"Test {index+1}", text_color, ellipse_color)
        
        # Paste the individual image into the grid image
        position = (col * 100, row * 100)  # X, Y
        grid_image.paste(image, position)

# Compression levels to use
compression_levels = [10, 50, 95]

# Save the grid image with different compression levels
for compression in compression_levels:
    filename = f"./tmp/complex/grid_image_quality_{compression}.jpg"
    grid_image.save(filename, "JPEG", quality=compression)
    print(f"Saved {filename} with compression level {compression}")