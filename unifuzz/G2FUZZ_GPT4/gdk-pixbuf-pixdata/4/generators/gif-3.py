from PIL import Image, ImageDraw
import os

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Generate a GIF with a limited color palette
def create_palette_limited_gif(output_path):
    # Define the size of the image and the color palette (limited to 8 colors here for demonstration)
    width, height = 200, 200
    palette = [(255, 0, 0), (0, 255, 0), (0, 0, 255),
               (255, 255, 0), (255, 0, 255), (0, 255, 255),
               (255, 255, 255), (0, 0, 0)]
    
    # Create a new image with the first color in the palette
    img = Image.new("P", (width, height), palette[0])
    # Set the palette of the image
    img.putpalette([val for color in palette for val in color])

    # Draw some shapes with the colors from the palette
    draw = ImageDraw.Draw(img)
    for i, color in enumerate(palette):
        draw.rectangle([width/8*i, 0, width/8*(i+1), height], fill=i)

    # Save the image as a GIF
    img.save(output_path)

# Create and save the GIF
output_path = os.path.join(output_dir, "palette_limited.gif")
create_palette_limited_gif(output_path)

print(f"GIF saved to {output_path}")