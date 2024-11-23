from PIL import Image, ImageDraw

# Create a directory for the output if it doesn't exist
import os
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Define the image size and background color
width, height = 300, 300
background_color = (255, 255, 255)  # White

# Function to create an image layer
def create_layer(shape, fill_color):
    img = Image.new("RGB", (width, height), color=background_color)
    draw = ImageDraw.Draw(img)
    if shape == 'rectangle':
        draw.rectangle([(50, 50), (250, 250)], fill=fill_color)
    elif shape == 'circle':
        draw.ellipse([(75, 75), (225, 225)], fill=fill_color)
    else:  # triangle
        draw.polygon([(150, 50), (50, 250), (250, 250)], fill=fill_color)
    return img

# Create individual layers
layer1 = create_layer('rectangle', 'red')
layer2 = create_layer('circle', 'green')
layer3 = create_layer('triangle', 'blue')

# Save the layers as a multi-page TIFF
layer1.save(
    os.path.join(output_dir, 'multi_layer.tiff'),
    save_all=True,
    append_images=[layer2, layer3],
    compression="tiff_deflate",
)

print("TIFF file with layers has been saved.")